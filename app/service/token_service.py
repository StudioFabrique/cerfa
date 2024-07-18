from fastapi import HTTPException, status
from jose import JWTError, jwt
from pydantic import BaseModel
import os
import datetime

# Configuration
SECRET_KE = os.getenv("SECRET_KEY")
SECRET_KEY = str(SECRET_KE)
if SECRET_KEY is None:
    SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

class TokenData(BaseModel):
    user_id: str | None = None

class TokenService:
    def __init__(self):
        self.secret_key = SECRET_KEY

    def generate_token(self, user_id: str, user_role: str, remember_me: bool) -> str:
        payload = {
            'id': user_id,
            'role':user_role,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30) if remember_me else datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
        }
        token = jwt.encode(payload, self.secret_key, algorithm="HS256")
        return token

    def verify_token(self, token: str) -> TokenData:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[ALGORITHM])
            user_id = payload.get("id")
            if user_id is None or not isinstance(user_id, str):
                raise credentials_exception
            token_data = TokenData(user_id=user_id)
        except JWTError:
            raise credentials_exception
        return token_data
