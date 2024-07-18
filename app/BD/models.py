from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float, LargeBinary, Table
from sqlalchemy.orm import relationship
from .database import Base



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    prenom = Column(String)
    nom = Column(String)
    password = Column(String, nullable=False)
    cfa_id = Column(Integer, ForeignKey('cfas.id'))
    employeur_id = Column(Integer, ForeignKey('employeurs.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))
    
    cfa = relationship("CFA", back_populates="users")
    employeur = relationship("Employeur", back_populates="users")
    role = relationship("Role", back_populates="users")

class Role(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    nom_role = Column(String)
    
    users = relationship("User", back_populates="role")

class Apprenant(Base):
    __tablename__ = "apprenants"
    
    id = Column(Integer, primary_key=True, index=True)
    nom_naissance = Column(String)
    nom_usage = Column(String)
    prenom = Column(String)
    sexe = Column(String)
    date_naissance = Column(DateTime)
    nationalite = Column(String)
    regime_social = Column(String)
    sportif_haut_niveau = Column(Boolean)
    reconnaissance_travailleur_handicape = Column(Boolean)
    situation_avant_contrat = Column(String)
    dernier_diplome_prepare = Column(String)
    derniere_annee_suivie = Column(String)
    intitule_precedent_diplome = Column(String)
    diplome_obtenu = Column(String)
    projet_creation_entreprise = Column(Boolean)
    numero = Column(String)
    rue = Column(String)
    complement = Column(String)
    code_postal = Column(String)
    commune = Column(String)
    telephone = Column(String)
    courriel = Column(String)
    
    representant_legal_id = Column(Integer, ForeignKey("representants_legaux.id"))
    employeur_id = Column(Integer, ForeignKey("employeurs.id"))

    formations = relationship("Formation", secondary="appartenir", back_populates="apprenants")
    representant_legal = relationship("RepresentantLegal", back_populates="apprenants")
    employeur = relationship("Employeur", back_populates="apprenants")
    contrats = relationship("Contrat", back_populates="apprenti")

class RepresentantLegal(Base):
    __tablename__ = "representants_legaux"
    
    id = Column(Integer, primary_key=True, index=True)
    nom_naissance = Column(String)
    prenom = Column(String)
    numero = Column(String)
    rue = Column(String)
    complement = Column(String)
    code_postal = Column(String)
    commune = Column(String)
    courriel = Column(String)
    
    apprenants = relationship("Apprenant", back_populates="representant_legal")

class Employeur(Base):
    __tablename__ = "employeurs"
    
    id = Column(Integer, primary_key=True, index=True)
    nom_entreprise = Column(String)
    numero_siret = Column(String)
    numero = Column(String)
    rue = Column(String)
    complement = Column(String)
    code_postal = Column(String)
    commune = Column(String)
    code_IDCC = Column(String)
    effectif = Column(Integer)
    code_activite_NAF = Column(String)
    employeur_specifique = Column(String)
    type_employeur = Column(String)
    courriel = Column(String)
    telephone = Column(String)
    
    apprenants = relationship("Apprenant", back_populates="employeur")
    maitres_apprentissage = relationship("MaitreApprentissage", back_populates="employeur")
    contrats = relationship("Contrat", back_populates="employeur")
    users = relationship("User", back_populates="employeur")

class MaitreApprentissage(Base):
    __tablename__ = "maitres_apprentissage"
    
    id = Column(Integer, primary_key=True, index=True)
    nom_naissance = Column(String)
    prenom = Column(String)
    date_naissance = Column(DateTime)
    courriel = Column(String)
    emploi_occupe = Column(String)
    diplome_obtenu = Column(String)
    niveau_diplome = Column(String)
    
    employeur_id = Column(Integer, ForeignKey("employeurs.id"))

    employeur = relationship("Employeur", back_populates="maitres_apprentissage")

class CFA(Base):
    __tablename__ = "cfas"
    
    id = Column(Integer, primary_key=True, index=True)
    cfa_enterprise = Column(Boolean)
    denomination_cfa = Column(String)
    n_uai_cfa = Column(String)
    numero = Column(String)
    rue = Column(String)
    complement = Column(String)
    code_postal = Column(String)
    commune = Column(String)
    n_siret = Column(String)
    
    users = relationship("User", back_populates="cfa")
    contrats = relationship("Contrat", back_populates="cfa")
    formations = relationship("Formation", back_populates="cfa")

class TypeContrat(Base):
    __tablename__ = "type_contrats"
    
    id = Column(Integer, primary_key=True, index=True)
    type_contrat = Column(String)
    
    contrats = relationship("Contrat", back_populates="type_contrat")

class Contrat(Base):
    __tablename__ = "contrats"
    
    id = Column(Integer, primary_key=True, index=True)
    date_debut_formation = Column(DateTime)
    type_derogation = Column(String)
    date_Avenant = Column(DateTime)
    date_conclusion = Column(DateTime)
    date_debut_contrat = Column(DateTime)
    date_fin_contrat = Column(DateTime)
    horraires = Column(String)
    lieu_signature = Column(String)
    dispo_ensemble_pieces = Column(Boolean)
    signature_cfa = Column(LargeBinary)
    signature_apprenti = Column(LargeBinary)
    signature_employeur = Column(LargeBinary)
    signature_responsable_legal = Column(LargeBinary)
    numero_de_contrat = Column(String)
    
    type_contrat_id = Column(Integer, ForeignKey("type_contrats.id"))
    apprenti_id = Column(Integer, ForeignKey("apprenants.id"))
    employeur_id = Column(Integer, ForeignKey("employeurs.id"))
    cfa_id = Column(Integer, ForeignKey("cfas.id"))
    remuneration_id = Column(Integer, ForeignKey("remunerations.id"))

    type_contrat = relationship("TypeContrat", back_populates="contrats")
    apprenti = relationship("Apprenant", back_populates="contrats")
    employeur = relationship("Employeur", back_populates="contrats")
    cfa = relationship("CFA", back_populates="contrats")
    remuneration = relationship("Remuneration", back_populates="contrats")

class Formation(Base):
    __tablename__ = "formations"
    
    id = Column(Integer, primary_key=True, index=True)
    nom_formation = Column(String)
    code_diplome = Column(String)
    code_rncp = Column(String)
    diplome_visé = Column(String)
    
    cfa_id = Column(Integer, ForeignKey("cfas.id"))
    lieu_id = Column(Integer, ForeignKey("lieu.id"))
    donneesFormation_id = Column(Integer, ForeignKey("donneesFormation.id"))
    
    apprenants = relationship("Apprenant", secondary="appartenir", back_populates="formations")
    cfa = relationship("CFA", back_populates="formations")
    donneesFormation = relationship("DonneesFormation", back_populates="formations")
    lieu = relationship("Lieu", back_populates="formations")

class DonneesFormation(Base):
    __tablename__='donneesFormation'

    id = Column(Integer, primary_key=True, index=True)
    date_debut_formation = Column(DateTime)
    date_prevue_examen = Column(DateTime)
    duree_formation = Column(String)
    annee_formation = Column(String)

    formations = relationship("Formation", back_populates="donneesFormation")

class Lieu(Base):
    __tablename__="lieu"

    id = Column(Integer, primary_key=True, index=True)
    denomination_lieu_formation = Column(String)
    n_uai = Column(String)
    n_siret = Column(String)
    numero = Column(String)
    rue = Column(String)
    complement = Column(String)
    code_postal = Column(String)
    commune = Column(String)

    formations = relationship("Formation", back_populates="lieu")

class Remuneration(Base):
    __tablename__ = "remunerations"
    
    id = Column(Integer, primary_key=True, index=True)
    repas = Column(Integer)
    type_remuneration = Column(String)
    logement = Column(Float)
    caisse_retraite = Column(String)
    autre = Column(Float)
    salaire_brut_total = Column(Float)
    debut_annee1 = Column(DateTime)
    fin_annee1 = Column(DateTime)
    pourcentage_annee1 = Column(Float)
    debut_annee2 = Column(DateTime)
    fin_annee2 = Column(DateTime)
    pourcentage_annee2 = Column(Float)
    debut_annee3 = Column(DateTime)
    fin_annee3 = Column(DateTime)
    pourcentage_annee3 = Column(Float)
    debut_annee4 = Column(DateTime)
    fin_annee4 = Column(DateTime)
    pourcentage_annee4 = Column(Float)
    
    contrats = relationship("Contrat", back_populates="remuneration")

Appartenir = Table(
    "appartenir",
    Base.metadata,
    Column("apprenants_id", Integer, ForeignKey("apprenants.id"), primary_key=True),
    Column("formations_id", Integer, ForeignKey("formations.id"), primary_key=True),
)
