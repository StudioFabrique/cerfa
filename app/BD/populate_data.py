from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from .database import Base
from passlib.context import CryptContext
from .models import User, Role, Apprenant, MaitreApprentissage, Employeur, CFA, TypeContrat, Contrat, Formation, Remuneration, RepresentantLegal, Appartenir, Lieu, DonneesFormation

# Configure the database connection
DATABASE_URL = "postgresql+psycopg2://noa:noa@localhost/cerfa"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed_password = pwd_context.hash("password")

# Initialize Faker
fake = Faker()

# Generate random data
def create_role(session, nom_role):
    role = Role(
        nom_role=nom_role
    )
    session.add(role)
    session.commit()
    return role

def create_user(session, role, cfa=None, employeur=None):
    user = User(
        email=fake.email(),
        is_active=True,
        created_at=datetime.now(),
        prenom=fake.first_name(),
        nom=fake.last_name(),
        password=hashed_password,
        role_id=role.id,
        cfa_id=cfa.id if cfa else None,
        employeur_id=employeur.id if employeur else None
    )
    session.add(user)
    session.commit()
    return user

def create_apprenant(session, employeur):
    apprenant = Apprenant(
        nom_naissance=fake.last_name(),
        nom_usage=fake.last_name(),
        prenom=fake.first_name(),
        sexe=fake.random_element(elements=("M", "F")),
        date_naissance=fake.date_of_birth(),
        nationalite=fake.country(),
        regime_social=fake.word(),
        sportif_haut_niveau=fake.boolean(),
        reconnaissance_travailleur_handicape=fake.boolean(),
        situation_avant_contrat=fake.word(),
        dernier_diplome_prepare=fake.word(),
        derniere_annee_suivie=fake.word(),
        intitule_precedent_diplome=fake.word(),
        diplome_obtenu=fake.word(),
        projet_creation_entreprise=fake.boolean(),
        numero=fake.building_number(),
        rue=fake.street_name(),
        complement=fake.secondary_address(),
        code_postal=fake.postcode(),
        commune=fake.city(),
        telephone=fake.phone_number(),
        courriel=fake.email(),
        representant_legal_id=None,
        employeur_id=employeur.id
    )
    session.add(apprenant)
    session.commit()
    return apprenant

def create_maitre_apprentissage(session, employeur):
    maitre = MaitreApprentissage(
        nom_naissance=fake.last_name(),
        prenom=fake.first_name(),
        date_naissance=fake.date_of_birth(),
        courriel=fake.email(),
        emploi_occupe=fake.job(),
        diplome_obtenu=fake.word(),
        niveau_diplome=fake.word(),
        employeur_id=employeur.id
    )
    session.add(maitre)
    session.commit()
    return maitre

def create_employeur(session):
    code_IDCC = str(fake.random_int(min=1000, max =9999))
    effectif = fake.random_int(min=1, max=1000)
    code_activite_NAF = f"{fake.random_int(min=10, max=99)}.{fake.random_int(min=1, max=9)}"
    
    employeur_specifique_choices = ['PME', 'Grand Groupe', 'Indépendant', 'Association']
    employeur_specifique = fake.random_element(employeur_specifique_choices)
    
    type_employeur_choices = ['Privé', 'Public', 'Mixte']
    type_employeur = fake.random_element(type_employeur_choices)
    employeur = Employeur(
        nom_entreprise=fake.company(),
        numero_siret=fake.ean13(),
        numero=fake.building_number(),
        rue=fake.street_name(),
        complement=fake.secondary_address(),
        code_postal=fake.postcode(),
        commune=fake.city(),
        courriel=fake.email(),
        telephone=fake.phone_number(),
        code_IDCC=code_IDCC,
        effectif=effectif,
        code_activite_NAF=code_activite_NAF,
        employeur_specifique=employeur_specifique,
        type_employeur=type_employeur
    )
    session.add(employeur)
    session.commit()
    return employeur

def create_cfa(session):
    cfa = CFA(
        cfa_enterprise=fake.boolean(),
        denomination_cfa=fake.company(),
        n_uai_cfa=fake.ean8(),
        numero=fake.building_number(),
        rue=fake.street_name(),
        complement=fake.secondary_address(),
        code_postal=fake.postcode(),
        commune=fake.city(),
        n_siret=fake.ssn()
    )
    session.add(cfa)
    session.commit()
    return cfa

def create_type_contrat(session):
    type_contrat = TypeContrat(
        type_contrat=fake.word()
    )
    session.add(type_contrat)
    session.commit()
    return type_contrat

def create_contrat(session, type_contrat, apprenant, employeur, cfa):
    contrat = Contrat(
        type_contrat_id=type_contrat.id,
        apprenti_id=apprenant.id,
        employeur_id=employeur.id,
        cfa_id=cfa.id,
        type_derogation=fake.word(),
        date_debut_formation=fake.date_time(),
        date_Avenant=fake.date_time(),
        date_conclusion=fake.date_time(),
        date_debut_contrat=fake.date_time(),
        date_fin_contrat=fake.date_time(),
        lieu_signature=fake.city(),
        dispo_ensemble_pieces=fake.boolean(),
        signature_cfa=fake.binary(length=64),
        signature_apprenti=fake.binary(length=64),
        signature_employeur=fake.binary(length=64),
        signature_responsable_legal=fake.binary(length=64),
        numero_de_contrat=fake.ssn(),
        remuneration_id=None
    )
    session.add(contrat)
    session.commit()
    return contrat

def create_lieu(session):
    lieu = Lieu(
        denomination_lieu_formation=fake.company(),
        n_uai=fake.ean8(),
        n_siret=fake.ssn(),
        numero=fake.building_number(),
        rue=fake.street_name(),
        complement=fake.secondary_address(),
        code_postal=fake.postcode(),
        commune=fake.city()
    )
    session.add(lieu)
    session.commit()
    return lieu

def create_donnees_formation(session):
    donnees_formation = DonneesFormation(
        date_debut_formation=fake.date_time(),
        date_prevue_examen=fake.date_time(),
        duree_formation=fake.word(),
        annee_formation=fake.year()
    )
    session.add(donnees_formation)
    session.commit()
    return donnees_formation

def create_formation(session, cfa):
    lieu = create_lieu(session)
    donnees_formation = create_donnees_formation(session)
    formation = Formation(
        nom_formation=fake.word(),
        code_diplome=fake.word(),
        code_rncp=fake.word(),
        diplome_visé=fake.word(),
        cfa_id=cfa.id,
        lieu_id=lieu.id,
        donneesFormation_id=donnees_formation.id
    )
    session.add(formation)
    session.commit()
    return formation

def create_remuneration(session):
    remuneration = Remuneration(
        repas=fake.random_int(min=0, max=100),
        type_remuneration=fake.word(),
        logement=fake.pyfloat(left_digits=4, right_digits=2, min_value=0, max_value=1000),
        caisse_retraite=fake.word(),
        autre=fake.pyfloat(left_digits=4, right_digits=2, min_value=0, max_value=1000),
        salaire_brut_total=fake.pyfloat(left_digits=4, right_digits=2, min_value=0, max_value=10000),
        debut_annee1=fake.date_time(),
        fin_annee1=fake.date_time(),
        pourcentage_annee1=fake.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=100),
        debut_annee2=fake.date_time(),
        fin_annee2=fake.date_time(),
        pourcentage_annee2=fake.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=100),
        debut_annee3=fake.date_time(),
        fin_annee3=fake.date_time(),
        pourcentage_annee3=fake.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=100),
        debut_annee4=fake.date_time(),
        fin_annee4=fake.date_time(),
        pourcentage_annee4=fake.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=100)
    )
    session.add(remuneration)
    session.commit()
    return remuneration

def create_representant_legal(session):
    representant_legal = RepresentantLegal(
        nom_naissance=fake.last_name(),
        prenom=fake.first_name(),
        numero=fake.building_number(),
        rue=fake.street_name(),
        complement=fake.secondary_address(),
        code_postal=fake.postcode(),
        commune=fake.city(),
        courriel=fake.email()
    )
    session.add(representant_legal)
    session.commit()
    return representant_legal

# Main function to populate the database
def main():
    session = SessionLocal()

    # Create roles
    roles = [create_role(session, f"ROLE_{role}") for role in ["admin", "membre", "gestionnaire"]]  # Creating specific roles

    # Create CFAs and employeurs
    cfas = [create_cfa(session) for _ in range(5)]
    employeurs = [create_employeur(session) for _ in range(5)]

    # Create users
    for _ in range(10):
        if fake.boolean():
            create_user(session, fake.random_element(roles), cfa=fake.random_element(cfas), employeur=None)
        else:
            create_user(session, fake.random_element(roles), cfa=None, employeur=fake.random_element(employeurs))

    # Create apprenants
    apprenants = []
    for employeur in employeurs:
        for _ in range(10):  # 10 apprenants par employeur
            apprenants.append(create_apprenant(session, employeur))

    # Create maitres d'apprentissage
    for employeur in employeurs:
        for _ in range(2):  # Deux maitres par employeur
            create_maitre_apprentissage(session, employeur)

    # Create type_contrats
    type_contrats = [create_type_contrat(session) for _ in range(5)]

    # Create contrats
    for apprenant in apprenants:
        create_contrat(session, fake.random_element(type_contrats), apprenant, apprenant.employeur, fake.random_element(cfas))

    # Create formations
    for cfa in cfas:
        for _ in range(2):  # Deux formations par CFA
            formation = create_formation(session, cfa)
            for apprenant in apprenants:  # Associer chaque apprenant à la formation créée
                appartenir_entry = Appartenir.insert().values(apprenants_id=apprenant.id, formations_id=formation.id)
                session.execute(appartenir_entry)

    # Create remunerations
    for _ in range(10):
        create_remuneration(session)

    # Create representants legaux
    for _ in range(10):
        create_representant_legal(session)

    session.commit()

if __name__ == "__main__":
    main()