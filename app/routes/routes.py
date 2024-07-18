from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/database", response_class=HTMLResponse)
def read_root():
    return "<html><body><h1>Database Endpoint</h1></body></html>"