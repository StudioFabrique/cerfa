from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.responses import JSONResponse
from ..BD.models import Contrat, User, Apprenant, Employeur, TypeContrat
from ..service.dependencies import get_current_user, get_db
import base64

app = FastAPI()
router = APIRouter(
    prefix="/accueil",
    tags=["accueil"]
)

@router.get("/contracts/CFAUnsigned")
async def get_contracts_CFAUnsigned(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
    select(
        Apprenant.nom_usage,
        Apprenant.prenom,
        Apprenant.date_naissance,
        Employeur.nom_entreprise,
        TypeContrat.type_contrat,
        Contrat.id,
        Contrat.signature_apprenti,
        Contrat.signature_cfa,
        Contrat.signature_employeur
    ).join(Contrat, Apprenant.id == Contrat.apprenti_id)
     .join(Employeur, Employeur.id == Contrat.employeur_id)
     .join(TypeContrat, TypeContrat.id == Contrat.type_contrat_id)
     .where(Contrat.signature_cfa == None)
    )

    all_data = result.all()
    
    apprenants = []
    for row in all_data:
        apprenants.append({
            "nom_usage": row[0],
            "prenom": row[1],
            "date_naissance": row[2],
            "nom_entreprise": row[3],
            "type_contrat": row[4],
            "id":row[5],
            "signature_apprenti": base64.b64encode(row[6]).decode('utf-8') if row[6] else None,
            "signature_cfa": base64.b64encode(row[7]).decode('utf-8') if row[7] else None,
            "signature_employeur": base64.b64encode(row[8]).decode('utf-8') if row[8] else None
        })

    return apprenants



@router.get("/contracts/CFAsigned")
async def get_contracts_CFAsigned(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
    select(
        Apprenant.nom_usage,
        Apprenant.prenom,
        Apprenant.date_naissance,
        Employeur.nom_entreprise,
        TypeContrat.type_contrat,
        Contrat.id,
        Contrat.signature_apprenti,
        Contrat.signature_cfa,
        Contrat.signature_employeur
    ).join(Contrat, Apprenant.id == Contrat.apprenti_id)
     .join(Employeur, Employeur.id == Contrat.employeur_id)
     .join(TypeContrat, TypeContrat.id == Contrat.type_contrat_id)
     .where(Contrat.signature_cfa != None)
    )

    all_data = result.all()
    
    apprenants = []
    for row in all_data:
        apprenants.append({
            "nom_usage": row[0],
            "prenom": row[1],
            "date_naissance": row[2],
            "nom_entreprise": row[3],
            "type_contrat": row[4],
            "id":row[5],
            "signature_apprenti": base64.b64encode(row[6]).decode('utf-8') if row[6] else None,
            "signature_cfa": base64.b64encode(row[7]).decode('utf-8') if row[7] else None,
            "signature_employeur": base64.b64encode(row[8]).decode('utf-8') if row[8] else None
        })

    return apprenants



@router.get("/contracts/CFA")
async def get_contracts_CFA(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(
    select(
        Apprenant.nom_usage,
        Apprenant.prenom,
        Apprenant.date_naissance,
        Employeur.nom_entreprise,
        TypeContrat.type_contrat,
        Contrat.id,
        Contrat.signature_apprenti,
        Contrat.signature_cfa,
        Contrat.signature_employeur
    ).join(Contrat, Apprenant.id == Contrat.apprenti_id)
     .join(Employeur, Employeur.id == Contrat.employeur_id)
     .join(TypeContrat, TypeContrat.id == Contrat.type_contrat_id)
    )

    all_data = result.all()
    
    apprenants = []
    for row in all_data:
        apprenants.append({
            "nom_usage": row[0],
            "prenom": row[1],
            "date_naissance": row[2],
            "nom_entreprise": row[3],
            "type_contrat": row[4],
            "id":row[5],
            "signature_apprenti": base64.b64encode(row[6]).decode('utf-8') if row[6] else None,
            "signature_cfa": base64.b64encode(row[7]).decode('utf-8') if row[7] else None,
            "signature_employeur": base64.b64encode(row[8]).decode('utf-8') if row[8] else None
        })

    return apprenants

   

@router.get("/contratcts/Employeur")
async def get_contracts_Employeur(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User.employeur_id).filter(User.id == current_user['user_id'] ))
    employeur_id = result.scalars().first()

    if(employeur_id):
        result2 = await db.execute(select(Contrat).filter(Contrat.employeur_id == employeur_id))
    contracts = result2.scalars().all()
    return contracts



@router.delete("/contracts/{id}")
async def delete_contract(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Contrat).filter(Contrat.id == id))
    contract = result.scalars().first()
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")
    await db.delete(contract)
    await db.commit()
    return {"message": "Contract deleted successfully"}

app.include_router(router)