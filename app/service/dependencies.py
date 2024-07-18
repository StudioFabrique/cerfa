from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from .token_service import TokenService
from pydantic import BaseModel
from ..BD.models import User
from sqlalchemy.future import select


# Configuration de la base de données
DATABASE_URL = "postgresql+asyncpg://noa:noa@localhost/cerfa"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# Contexte de cryptage des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Configuration OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class TokenData(BaseModel):
    user_id: str | None = None


async def get_current_user(token: str = Depends(oauth2_scheme), token_service: TokenService = Depends(TokenService)) -> dict:
    token_data = token_service.verify_token(token)
    if token_data is None or token_data.user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    async with AsyncSessionLocal() as session:
        user_id = int(token_data.user_id)
        result = await session.execute(select(User).filter(User.id == user_id))
        user = result.scalars().first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"user_id": user.id}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session