from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi import APIRouter

router = APIRouter()

app = FastAPI()
@router.get("/formulaire_entre1", response_class=HTMLResponse)
def read_root():
    return """
        <html>
            <head>
                <title>Formulaire apprenti</title>
            </head>
            <body>
                <form action="/resultat" method="post">
                    <h2>L'employeur</h2>
                    <label for="public">employeur public ou privé:</label>
                    <select name="public" id="public">
                        <option value="1">Public</option>
                        <option value="0">Privé</option>
                        </select><br>
                    <label for="nom_prénom">Nom et prénom ou dénomination :</label>
                    <input type="text" id="nom_prénom" name="nom_prénom"><br>
                    <label for="numero">Numéro:</label>
                    <input type="text" id="numero" name="numero"><br>
                    <label for="rue">Rue:</label>
                    <input type="text" id="rue" name="rue"><br>
                    <label for="complement">Complément:</label>
                    <input type="text" id="complement" name="complement"><br>
                    <label for="commune">Commune:</label>
                    <input type="text" id="commune" name="commune"><br>
                    <label for="postal">Code postal:</label>
                    <input type="text" id="postal" name="postal"><br>
                    <label for="telephone">Téléphone:</label>
                    <input type="text" id="telephone" name="telephone"><br>
                    <label for="courriel">Courriel:</label>
                    <input type="text" id="courriel" name="courriel"><br>
                    <label for="siret">N°SIRET:</label>
                    <input type="text" id="siret" name="siret"><br>
                    <label for="type_employeur">Type d'employeur :</label>
                    <select name="type_employeur" id="type_employeur">
                        <option value="11">Entreprise inscrite au répertoire des métiers ou au registre des entreprises pour l'Alsace-Moselle</option>
                        <option value="12">Entreprise inscrite uniquement au registre du commerce et des sociétés</option>
                        <option value="13">Entreprises dont les salariés relèvent de la mutualité sociale agricole</option>
                        <option value="14">Profession libérale</option>
                        <option value="15">Contrat de professionnalisation</option>
                        <option value="16">Autre employeur privé</opErtion>
                        <option value="21">Service de l'Etat</option>
                        <option value="22">Commune</option>
                        <option value="23">Département</option>
                        <option value="24">Région</option>
                        <option value="25">Etablissement public hospitalier</option>
                        <option value="26">Etablissement public local d'enseignement</option>
                        <option value="27">Etablissement public administratif de l'Etat</option>
                        <option value="28">Etablissement public administratif local</option>
                        <option value="29">Autre employeur public</option>
                        <option value="30">Etablissement public industriel et commercial</option>
                    </select><br>
                    <label for="spe_employeur">Employeur specifique :</label>
                    <select name="spe_employeur" id="spe_employeur">
                        <option value="1">Entreprise inscrite au répertoire des métiers ou au registre des entreprises pour l'Alsace-Moselle</option>
                        <option value="2">Entreprise inscrite uniquement au registre du commerce et des sociétés</option>
                        <option value="3">Entreprises dont les salariés relèvent de la mutualité sociale agricole</option>
                        <option value="4">Profession libérale</option>
                        <option value="0">Aucun de ces cas</option>
                    </select><br>
                    <label for="NAF">Code activité de l'entreprise (NAF):</label>
                    <input type="text" id="NAF" name="NAF"><br>
                    <label for="effectif">Effectif total salariés de l'entreprise :</label>
                    <input type="text" id="effectif" name="effectif"><br>
                    <label for="idcc">Code IDCC de la convention collective applicable :</label>
                    <input type="text" id="idcc" name="idcc"><br>

                    <h2>Le maitre d'apprentissage</h2>
                    <label for="nom_m">Nom de naissance :</label>
                    <input type="text" id="nom_m" name="nom_m"><br>
                    <label for="prénom_m">Prénom :</label>
                    <input type="text id="prénom_m" name="prénom_m"><br>
                    <label for="date_naissance">Date de naissance :</label>
                    <input type="date" id="date_naissance" name="date_naissance"><br>
                    <label for="NIR">NIR :</label>
                    <input type="text id="NIR" name="NIR"><br> 
                    <label for="courriel_m">Courriel :</label>
                    <input type="email" id="courriel_m" name="courriel_m"><br>
                    <label for="emploi">Emploi occupé :</label>
                    <input type="text" id="emploi" name="emploi"><br>
                    <label fore="diplome_eleve"> Diplôme ou titre le plus élevé obtenu :</label>
                    <select name="diplome_eleve" id="diplome_eleve">
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
                        <option value="41">Baccalauréat professionnel</option>
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
                    <label for="niveau">Niveau du diplôme le plus élevé :</label>
                    <select name="niveau" id="niveau">
                        <option value="3">CAP, BEP</option>
                        <option value="4">Baccalauréat</option>
                        <option value="5">DEUG, BTS, DUT, DEUST</option>
                        <option value="6">Licence, licence professionnelle, BUT, Maîtrise</option>
                        <option value="7">Master, diplôme d'études approfondies, diplôme d'études supérieures spécialisées, diplôme d'ingénieur</option>
                        <option value="8">Doctorat, habilitation à diriger des recherches</option>
                    </select>
                    <br>

                    <h2>Le maitre d'apprentissage n°2 (optionel)</h2>
                    <label for="nom_m2">Nom de naissance :</label>
                    <input type="text" id="nom_m2" name="nom_m2"><br>
                    <label for="prénom_m2">Prénom :</label>
                    <input type="text id="prénom_m2" name="prénom_m2"><br>
                    <label for="date_naissance2">Date de naissance :</label>
                    <input type="date" id="date_naissance2" name="date_naissance2"><br>
                    <label for="NIR2">NIR :</label>
                    <input type="text id="NIR2" name="NIR2"><br> 
                    <label for="courriel_m2">Courriel :</label>
                    <input type="email" id="courriel_m2" name="courriel_m2"><br>
                    <label for="emploi2">Emploi occupé :</label>
                    <input type="text" id="emploi2" name="emploi2"><br>
                    <label fore="diplome_eleve2"> Diplôme ou titre le plus élevé obtenu :</label>
                    <select name="diplome_eleve2" id="diplome_eleve2">
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
                        <option value="41">Baccalauréat professionnel</option>
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
                    <label for="niveau2">Niveau du diplôme le plus élevé :</label>
                    <select name="niveau2" id="niveau2">
                        <option value="3">CAP, BEP</option>
                        <option value="4">Baccalauréat</option>
                        <option value="5">DEUG, BTS, DUT, DEUST</option>
                        <option value="6">Licence, licence professionnelle, BUT, Maîtrise</option>
                        <option value="7">Master, diplôme d'études approfondies, diplôme d'études supérieures spécialisées, diplôme d'ingénieur</option>
                        <option value="8">Doctorat, habilitation à diriger des recherches</option>
                    </select><br>
                    <button type="submit">Valider</button>
                </form>
            </body>
        </html>
    """


@app.post("/resultat_entre")
def create_entre(
    public: bool = Form(...),
    nom_prénom: str = Form(...),
    numero: int = Form(...),
    rue: str = Form(...),
    complement: str = Form("None"),
    commune: str = Form(...),
    postal: int = Form(...),
    telephone: str = Form(...),
    courriel: str = Form(...),
    siret: int = Form(...),
    type_employeur: int = Form(...),
    spe_employeur: int = Form(...),
    NAF: str = Form(...),
    effectif: int = Form(...),
    idcc: int = Form(...),

    nom_m: str = Form(...),
    prénom_m: str = Form(...),
    date_naissance: str = Form(...),
    courriel_m: str = Form(...),
    emploi: str = Form(...),
    diplome_eleve: str = Form(...),
    niveau_diplome: str = format(...),

    nom_m2: str = Form("None"),
    prénom_m2: str = Form("None"),
    date_naissance2: str = Form("None"),
    courriel_m2: str = Form("None"),
    emploi2: str = Form("None"),
    diplome_eleve2: str = Form("None"),
    niveau_diplome2: str = format("None"),
):
    Employeur = {
        "public": public,
        "nom_prénom": nom_prénom,
        "numero": numero,
        "rue": rue,
        "complement": complement,
        "commune": commune,
        "postal": postal,
        "telephone": telephone,
        "courriel": courriel,
        "siret": siret,
        "NAF": NAF,
        "type_employeur": type_employeur,
        "spe_employeur": spe_employeur,
        "effectif": effectif,
        "idcc": idcc
        }

    maitre_app = {
        "nom_m": nom_m,
        "prénom_m": prénom_m,
        "date_naissance": date_naissance,
        "courriel_m": courriel_m,
        "emploi": emploi,
        "diplome_eleve": diplome_eleve,
        "niveau_diplome": niveau_diplome
    }

    maitre_app2 = {
        "nom_m2": nom_m2,
        "prénom_m2": prénom_m2,
        "date_naissance2": date_naissance2,
        "courriel_m2": courriel_m2,
        "emploi2": emploi2,
        "diplome_eleve2": diplome_eleve2,
        "niveau_diplome2": niveau_diplome2
    }

    resultat = {
        "Employeur": Employeur,
        "maitre_app": maitre_app,
        "maitre_app2": maitre_app2
    }   
    return resultat