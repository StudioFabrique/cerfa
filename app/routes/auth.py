from fastapi import FastAPI, Form, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..BD.database import Base
from ..BD.models import User
from ..service.token_service import TokenService
from ..service.dependencies import get_db, engine, verify_password

app = FastAPI()
router = APIRouter(
    prefix="/auth",
    tags=['auth']
)

token_service = TokenService()


@router.post("/")
async def authenticate(email: Annotated[str, Form()], password: Annotated[str, Form()], rememberMe: Annotated[bool, Form()], db: AsyncSession = Depends(get_db)):
    async with db.begin():
        result = await db.execute(select(User).filter(User.email == email))
        user = result.scalars().first()
    if user is None or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    user_id_str = str(user.id)
    user_role = str(user.role_id)
    token = token_service.generate_token(user_id_str, user_role, rememberMe)
    response_data = {"access": token,
                     "role": user.role_id,
                     "id": user.id}
    return JSONResponse(content=response_data)

app.include_router(router)

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    init_db()