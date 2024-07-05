from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.responses import JSONResponse
from ..BD.models import Contrat, User, Apprenant, Employeur, TypeContrat
from ..service.dependencies import get_current_user, get_db

app = FastAPI()
router = APIRouter(
    prefix="/header",
    tags=["header"]
)

@router.get("/cerfa")
async def get_nombre_signe(current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Contrat.signature_cfa).where(Contrat.signature_cfa != None))
    all_non_null = result.scalars().all()
    result2 = await db.execute(select(Contrat.signature_cfa).where(Contrat.signature_cfa == None))
    all_null = result2.scalars().all()
    int_count_null = len(all_null)
    int_count_non_null = len(all_non_null)
    int_count_total = int_count_non_null + int_count_null
    count_null = str(int_count_null)
    count_non_null = str(int_count_non_null)
    count_total = str(int_count_total)

    response_data = {
        "nombre_null": count_null,
        "nombre_non_null": count_non_null,
        "nombre_total": count_total
    }
    return response_data
