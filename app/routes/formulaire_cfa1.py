from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
    
router = APIRouter()

app = FastAPI()
@router.get("/formulaire_cfa1", response_class=HTMLResponse)
def read_root():
    return """
        <html>
            <body>
                <h1>Formulaire CFA</h1>

            </body>
            <form action="/resultat" method="post">
                <h2>La formation</h2>
                <label for="CFA">CFA d'entreprise :</label>
                <select name="CFA" id="CFA">
                    <option value="1">Oui</option>
                    <option value="0">Non</option>
                </select><br>
                <label for="nom_CFA">Dénomination du CFA responsable: </label>
                <input type="text" id="nom_CFA" name="nom_CFA"><br>
                <label for="UAI">N°UAI du CFA: </label>
                <input type="text" id="UAI" name="UAI"><br>
                <label for="diplome">Diplôme ou titre visé par l’apprenti :</label>
                <select name="diplome" id="diplome"><br>
                        <option value="80">Doctorat</option>
                        <option value="71">Master professionnel/DESS</option>
                        <option value="72">Master recherche/DEA</option>
                        <option value="73">Master indifférencié</option>
                        <option value="74">Diplôme d'ingénieur, diplôme d'école de commerce</option>
                        <option value="79">Autre diplôme ou titre de niveau bac+5 ou plus</option>
                        <option value="61">1ère année de Master</option>
                        <option value="62">Licence professionnelle</option>
                        <option value="63">Licence générale</option>
                        <option value="64">Bachelor Universitaire de technologie BUT</option>
                        <option value="69">Autre diplôme ou titre de niveau bac +3 ou 4</option>
                        <option value="54">Brevet de Technicien Supérieur</option>
                        <option value="55">Diplôme Universitaire de technologie</option>
                        <option value="58">Autre diplôme ou titre de niveau bac+2</option>
                        <option value="41">Baccalauréat sprofessionnel</option>
                        <option value="42">Baccalauréat général</option>
                        <option value="43">Baccalauréat technologique</option>
                        <option value="49">Autre diplôme ou titre de niveau bac</option>
                        <option value="33">CAP</option>
                        <option value="34">BEP</option>
                        <option value="35">Mention complémentaire</option>
                        <option value="38">Autre diplôme ou titre de niveau CAP/BEP</option>
                        <option value="25">Diplôme national du Brevet</option>
                        <option value="26">Certificat de formation générale</option>
                        <option value="13">Aucun diplôme ni titre professionnel</option>
                    </select><br>
                <label for="intitule">Intitulé précis :</label>
                <input type="text" id="intitule" name="intitule"><br>
                <label for="code">Code du diplôme :</label>
                <input type="text" id="code" name="code"><br>
                <label for="rncp">Code RNCP :</label>
                <input type="text" id="rncp" name="rncp"><br>
                
                <h2>Adresse du CFA responsable</h2>
                
                <label for="numero">Numéro:</label>
                <input type="text" id="numero" name="numero"><br>
                <label for="rue">Rue:</label>
                <input type="text" id="rue" name="rue"><br>
                <label for="complement">Complément:</label>
                <input type="text" id="complement" name="complement"><br>
                <label for="commune">Commune:</label>
                <input type="text" id="commune" name="commune"><br>

                <h2>Organisation de la formation en CFA :</h2>

                <label for="date_debut">Date de début de formation en CFA :</label>
                <input type="date" id="date_debut" name="date_debut"><br>
                <label for="date_fin">Date prévue de fin des épreuves ou examens :</label>
                <input type="date" id="date_fin" name="date_fin"><br>
                <label for="duree">Durée de la formation :</label>
                <input type="number" id="duree" name="duree" min="0"><br>

                <h2>Lieu principal de réalisation de la formation si différent du CFA responsable</h2>

                <label for="denomination">Dénomination du lieu de formation principal :</label>
                <input type="text" id="denomination" name="denomination"><br>
                <label for="UAI2">N° UAI :</label>
                <input type="text" id="UAI2" name="UAI2"><br>
                <label for="siret2">N° SIRET :</label>
                <input type="text" id="siret2" name="siret2"><br>

                <h2>Adresse du lieu de formation principal</h2>

                <label for="numero_f">Numéro:</label>
                <input type="text" id="numero_f" name="numero_f"><br>
                <label for="rue_f">Rue:</label>
                <input type="text" id="rue_f" name="rue_f"><br>
                <label for="complement_f">Complément:</label>
                <input type="text" id="complement_f" name="complement_f"><br>
                <label for="commune_f">Commune:</label>
                <input type="text" id="commune_f" name="commune_f"><br>

                <input type="submit" value="Valider">
            </form>
        </html>
    """

@router.put("/resultat_cfa")
def create_cfa(
    CFA: bool = Form(...),
    nom_CFA: str = Form(...),
    UAI: str = Form(...),
    diplome: str = Form(...),
    intitule: str = Form(...),
    code: str = Form(...),
    rncp: str = Form(...),

    numero: int = Form(...),
    rue: str = Form(...),
    complement: str = Form("None"),
    commune: str = Form(...),

    date_debut: str = Form(...),
    date_fin: str = Form(...),
    duree: str = Form(...),

    denomination: str = Form("None"),
    UAI2: str = Form("None"),
    siret2: str = Form("None"),

    numero_f: int = Form(...),
    rue_f: str = Form(...),
    complement_f: str = Form("None"),
    commune_f: str = Form(...)

):

    formation = {
        "CFA":CFA,  
        "nom_CFA":nom_CFA,
        "UAI":UAI,
        "diplome":diplome,
        "intitule":intitule,
        "code":code,
        "rncp":rncp,
    }

    Adresse_CFA_responsable= {
        "numero":numero,
        "rue":rue,
        "complement":complement,
        "commune":commune,
    }

    Organisation_formation={
        "date_debut":date_debut,
        "date_fin":date_fin,
        "duree":duree,
    }

    lieu_autre={
        "denomination":denomination,
        "UAI2":UAI2,
        "siret2":siret2,
    }
    adresse_autre={
        "numero_f":numero_f,
        "rue_f":rue_f,
        "complement_f":complement_f,
        "commune_f":commune_f
    }
    
    resultat={
        "formation":formation,
        "Adresse_CFA_responsable":Adresse_CFA_responsable,
        "Organisation_formation":Organisation_formation,
        "lieu_autre":lieu_autre,
        "adresse_autre":adresse_autre
    }