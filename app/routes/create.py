from fastapi import FastAPI, Form, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..BD.database import Base
from pydantic import BaseModel
from typing import Optional
from ..BD.models import User, Employeur, Role, CFA
from ..service.token_service import TokenService
from ..service.dependencies import get_db, engine, verify_password, get_current_user


app = FastAPI()
router = APIRouter(
    prefix="/create",
    tags=['create']
)

token_service = TokenService()

@router.get("/information")
async def get_information(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employeur.nom_entreprise))

    entreprise = result.scalars().all()


app.include_router(router)