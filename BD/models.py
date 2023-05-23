from fastapi import FastAPI
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()
@router.get("/database", response_class=HTMLResponse)

class User(Base):
    __tablename__ = "Apprenant"

    id_app = Column(Integer, primary_key=True, index=True)
    nom_naissance= Column(String)
    nom_usage= Column(String)
    prenom= Column(String)
    inscription_sportif_hn= Column(String)
    nom_legal= Column(String)
    prenom_legal= Column(String)
    nationalite= Column(String)
    date_naissance= Column(String)
    sexe= Column(String)
    commune_naissance= Column(String)
    handicape= Column(Boolean)
    situation= Column(String)
    diplome= Column(String)
    classe= Column(String)
    intitule_diplome= Column(String)
    diplome_eleve= Column(String)
    crea_entreprise= Column(Boolean)

    numero= Column(String)
    rue= Column(String)
    complement= Column(String)
    commune= Column(String)
    telephone= Column(String)
    courriel= Column(String)

    rue_r= Column(String)
    complement_r= Column(String)
    commune_r= Column(String)
    telephone_r= Column(String)
    courriel_r= Column(String)

    Entreprise = relationship("Entreprise", back_populates="Apprenant")
    CFA = relationship("CFA", back_populates="Apprenant")

class Item(Base):
    __tablename__ = "Entreprise"

    id_entre = Column(Integer, primary_key=True, index=True)
    public= Column(Boolean)
    nom_prénom= Column(String)
    numero= Column(String)
    rue= Column(String)
    complement= Column(String)
    commune= Column(String)
    postal= Column(String)
    telephone= Column(String)
    courriel= Column(String)
    siret= Column(String)
    type_employeur= Column(String)
    spe_employeur= Column(String)
    NAF= Column(String)
    effectif= Column(String)
    idcc= Column(String)

    nom_m= Column(String)
    prénom_m= Column(String)
    date_naissance= Column(String)
    courriel_m= Column(String)
    emploi= Column(String)
    diplome_eleve= Column(String)
    niveau_diplome= Column(String)

    nom_m2= Column(String)
    prénom_m2= Column(String)
    date_naissance2= Column(String)
    courriel_m2= Column(String)
    emploi2= Column(String)
    diplome_eleve2= Column(String)
    niveau_diplome2= Column(String)

    Apprenant = relationship("Apprenant", back_populates="Entreprise")

class cfa(Base):
    __tablename__ = "CFA"
    id_cfa = Column(Integer, primary_key=True, index=True)
    CFA= Column(Boolean)
    nom_CFA= Column(String)
    UAI= Column(String)
    diplome= Column(String)
    intitule= Column(String)
    code= Column(String)
    rncp= Column(String)

    numero= Column(String)
    rue= Column(String)
    complement= Column(String)
    commune= Column(String)

    date_debut= Column(String)
    date_fin= Column(String)
    duree= Column(String)

    denomination= Column(String)
    UAI2= Column(String)
    siret2= Column(String)

    numero_f= Column(String)
    rue_f= Column(String)
    complement_f= Column(String)
    commune_f= Column(String)

    Apprenant = relationship("Apprenant", back_populates="CFA")