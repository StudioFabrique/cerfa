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
    prefix="/edit",
    tags=['edit']
)

token_service = TokenService()

class UserUpdate(BaseModel):
    nom: Optional[str]
    prenom: Optional[str]
    email: Optional[str]

class CFAUpdate(BaseModel):
    n_siret: Optional[str]
    n_uai_cfa:Optional[str]
    denomination_cfa: Optional[str]
    commune: Optional[str]
    numero: Optional[str]
    rue: Optional[str]
    complement: Optional[str]
    code_postal: Optional[str]

@router.get("/users")
async def get_Users(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
    select(
        User.nom,
        User.prenom,
        User.email,
        User.id,
    )
    )

    all_data = result.all()
    
    users = []
    for row in all_data:
        users.append({
            "nom": row[0],
            "prenom": row[1],
            "email": row[2],
            "id": row[3]
            })

    return users

@router.get("/get/user/{id}")
async def get_user(id: int, current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(
            User.nom,
            User.prenom,
            User.email,
            Employeur.nom_entreprise,
            Role.nom_role, 
        ).join(User, Role.id == User.role_id).where(User.id == id)
    )

    user_data = result.first()
    
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    response_data = {
        "nom": user_data.nom,
        "prenom": user_data.prenom,
        "email": user_data.email,
        "nom_entreprise": user_data.nom_entreprise,
        "nom_role": user_data.nom_role,
    }

    return response_data

@router.get("/get/cfa")
async def get_cfa(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CFA))
    
    cfa_data = result.scalars().first()

    if cfa_data is None: 
        raise HTTPException(status_code=404, detail="CFA not found")
    
    response_data = {
        "n_siret": cfa_data.n_siret,
        "code_postal": cfa_data.code_postal,
        "n_uai_cfa": cfa_data.n_uai_cfa,
        "complement": cfa_data.complement,
        "commune": cfa_data.commune,
        "rue": cfa_data.rue,
        "numero": cfa_data.numero,
        "denomination_cfa": cfa_data.denomination_cfa
    }

    return response_data

@router.put("/user/{id}")
async def update_user(id: int, user_update: UserUpdate, current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == id))
    user = result.scalars().first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_data = user_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(user, key, value)
    
    await db.commit()
    await db.refresh(user)
    
    return {"message": "User updated successfully", "user": user}

@router.put("/cfa")
async def updata_cfa(cfa_update: CFAUpdate, current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CFA))
    cfa = result.scalars().first()

    if not cfa:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_data = cfa_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(cfa, key, value)
    
    await db.commit()
    await db.refresh(cfa)
    
    return {"message": "User updated successfully", "user": cfa}

    
@router.delete("/delete/user/{id}")
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(user)
    await db.commit()
    return {"message": "User deleted successfully"}


app.include_router(router)