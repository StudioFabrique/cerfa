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

class EmployeurUpdate(BaseModel):
    nom_entreprise: Optional[str]
    numero_siret: Optional[str]
    numero: Optional[str]
    rue: Optional[str]
    complement: Optional[str]
    code_postal: Optional[str]
    commune: Optional[str]
    code_IDCC: Optional[str]
    effectif: Optional[str]
    code_activite_NAF: Optional[str]
    courriel: Optional[str]
    telephone: Optional[str]

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

@router.get("/employeurs")
async def get_Employeurs(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
    select(
        Employeur.id,
        Employeur.courriel,
        Employeur.nom_entreprise,
        Employeur.telephone,
    )
    )

    all_data = result.all()
    
    users = []
    for row in all_data:
        users.append({
            "id": row[0],
            "courriel": row[1],
            "nom_entreprise": row[2],
            "telephone": row[3]
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

router.get("/get/employeur/{id}")
async def get_employeur(id: int, current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(
            Employeur.nom_entreprise,
            Employeur.numero_siret,
            Employeur.numero,
            Employeur.rue,
            Employeur.complement, 
            Employeur.code_postal,
            Employeur.commune,
            Employeur.code_IDCC,
            Employeur.effectif,
            Employeur.code_activite_NAF,
            Employeur.courriel,
            Employeur.telephone
        ).where(Employeur.id == id)
    )

    user_data = result.first()
    
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    response_data = {
        "nom_entreprise": user_data.nom_entreprise,
        "numero_siret": user_data.numero_siret,
        "numero": user_data.numero,
        "rue": user_data.rue,
        "complement": user_data.complement,
        "code_postal": user_data.code_postal,
        "commune": user_data.commune,
        "code_IDCC": user_data.code_IDCC,
        "effectif": user_data.effectif, 
        "code_activite_NAF": user_data.code_activite_NAF,
        "courriel": user_data.courriel,
        "telephone": user_data.telephone
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

@router.delete("/delete/employeur/{id}")
async def delete_employeur(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employeur).filter(Employeur.id == id))
    employeur = result.scalars().first()
    if not employeur:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(employeur)
    await db.commit()
    return {"message": "User deleted successfully"}


app.include_router(router)