from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from .formulaire_app1 import create_app
from .formulaire_cfa1 import create_cfa
from .formulaire_entre1 import create_entre

router = APIRouter()
@router.get("/resultat", response_class=HTMLResponse)
def read_root():
    return create_app