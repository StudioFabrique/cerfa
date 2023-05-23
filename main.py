from fastapi import FastAPI
from routes import formulaire_app1, formulaire_entre1, formulaire_cfa1, resultat
from fastapi.responses import HTMLResponse
from .BD import database, models


app = FastAPI()

app.include_router(formulaire_app1.router)
app.include_router(formulaire_entre1.router)
app.include_router(formulaire_cfa1.router)
app.include_router(resultat.router)
app.include_router(database.router)
app.include_router(models.router)

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
