from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user:password@localhost/db_name"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

router = APIRouter()
@router.get("/database", response_class=HTMLResponse)
def read_root():
    return """"""
