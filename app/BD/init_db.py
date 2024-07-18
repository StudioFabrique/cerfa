
from models import User, Role, Apprenant, RepresentantLegal, Employeur, MaitreApprentissage, CFA, TypeContrat, Contrat, Formation, Remuneration, Appartenir
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Créez toutes les tables
    Base.metadata.create_all(bind=engine)
    print("Toutes les tables ont été créées.")

# Exécuter le script
if __name__ == "__main__":
    init_db()