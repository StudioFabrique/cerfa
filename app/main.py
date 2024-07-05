from fastapi import FastAPI
from .routes import formulaire_app1, formulaire_entre1, formulaire_cfa1, resultat, auth, accueil, pageheadercerfa
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from .BD.database import engine, Base
from .routes.routes import router as my_router



app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



Base.metadata.create_all(bind=engine)

app.include_router(my_router)

app.include_router(pageheadercerfa.router)

app.include_router(auth.router)

app.include_router(accueil.router)


# app.include_router(formulaire_app1.router)
# app.include_router(formulaire_entre1.router)
# app.include_router(formulaire_cfa1.router)
# app.include_router(resultat.router)
# app.include_router(database.router)
# app.include_router(models.router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
        <html>
            <body>
                <h1>Bienvenue sur ma page d'accueil</h1>
                <p><a href="/formulaire_app1">formulaire apprenant</a></p>
                <p><a href="/formulaire_entre1">formulaire entreprise</a></p>
                <p><a href="/formulaire_cfa1">formulaire CFA</a></p>
            </body>
        </html>
    """
