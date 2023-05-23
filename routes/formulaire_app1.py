from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi import APIRouter

router = APIRouter()

app = FastAPI()
@router.get("/formulaire_app1", response_class=HTMLResponse)
def read_root():
    return """
        <html>
            <head>
                <title>Formulaire entreprise</title>
            </head>
            <body>
                <form action="/resultat" method="post">
                    <h2>Identité</h2>
                    <label for="nom_naissance">Nom de naissance:</label>
                    <input type="text" id="nom_naissance" name="nom_naissance"><br>
                    <label for="nom_usage">Nom d'usage:</label>
                    <input type="text" id="nom_usage" name="nom_usage"><br>
                    <label for="prenom">Premier prénom:</label>
                    <input type="text" id="prenom" name="prenom"><br>
                    <label for="date_naissance">Date de naissance:</label>
                    <input type="date" id="date_naissance" name="date_naissance"><br>
                    <label for="sexe">Sexe:</label>
                    <select id="sexe" name="sexe">
                        <option value="M">M</option>
                        <option value="F">F</option>
                    </select><br>
                    <label for="departement_naissance">Département de naissance:</label>
                    <input type="text" id="departement_naissance" name="departement_naissance"><br>
                    <label for="commune_naissance">Commune de naissance:</label>
                    <input type="text" id="commune_naissance" name="commune_naissance"><br>
                    <label for="nationalite">Nationalité:</label>
                    <select id="nationalite" name="nationalite">
                        <option value="1">Français</option>
                        <option value="2">Union Européenne</option>
                        <option value="3">Etranger hors Union Européenne</option>
                    </select><br>
                    <label for="inscription_sportif_hn">Inscription sur la liste des sportifs de haut niveau :</label>
                    <select name="inscription_sportif_hn" id="inscription_sportif_hn">
                        <option value="1">Oui</option>
                        <option value="0">Non</option>
                    </select><br>
                    <label for="handicape">Déclare bénéficier de la reconnaissance travailleur handicapé :</label>
                    <select name="handicape" id="handicape">
                        <option value="1">Oui</option>
                        <option value="0">Non</option>
                        </select><br>
                    <label for="situation">Situation avant contrat :</label>
                    <select name="situation" id="situation"
                        <option value="1">Scolaire</option>
                        <option value="2">Prépa apprentissage</option>
                        <option value="3">Etudiant</option>
                        <option value="4">Contrat d'apprentissage</option>
                        <option value="5">Contrat de professionnalisation</option>
                        <option value="6">Contrat aidé</opErtion>
                        <option value="7">En formation, au CFA sous statut de stagiaire de la formation professionnelle</option>
                        <option value="8">En formation, au CFA sans contrat sous statut de stagiaire de la formation professionnelle</option>
                        <option value="9">Autres situations sous statut de stagiaire de la formation professionnelle</option>
                        <option value="10">Salarié</option>
                        <option value="11">Personne à la recherche d un emploi (inscrite ou non à Pôle Emploi)</option>
                        <option value="12">Inactif</option>
                    </select><br>
                    <label for="diplome">Dernier diplôme ou titre préparé :</label>
                    <select name="diplome" id="diplome">
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
                    <label for="classe"> Dernière classe / année suivie :</label>
                    <input type="text" id="classe" name="classe"><br>
                    <label for="annee">Dernière année ou classe suivie :</label>
                    <select id="annee" name="annee">
                        <option value="01">L’apprenti a suivi la dernière année du cycle de formation et a obtenu le diplôme ou titre</option>
                        <option value="11">L’apprenti a suivi la 1ère année du cycle et l’a validée (examens réussis mais année non diplômante)</option>
                        <option value="12">L’apprenti a suivi la 1ère année du cycle mais ne l’a pas validée (échec aux examens, interruption ou abandon de formation)</option>
                        <option value="21">L’apprenti a suivi la 2è année du cycle et l’a validée (examens réussis mais année non diplômante)</option>
                        <option value="22">L’apprenti a suivi la 2è année du cycle mais ne l’a pas validée (échec aux examens, interruption ou abandon de formation)</option>
                        <option value="31">L’apprenti a suivi la 3è année du cycle et l’a validée (examens réussis mais année non diplômante, cycle adaptés)</option>
                        <option value="32">L’apprenti a suivi la 3è année du cycle mais ne l’a pas validée (échec aux examens, interruption ou abandon de formation)</option>
                        <option value="40">L’apprenti a achevé le 1er cycle de l’enseignement secondaire (collège)</option>
                        <option value="41">L’apprenti a interrompu ses études en classe de 3è</option>
                        <option value="42">L’apprenti a interrompu ses études en classe de 4è</option>
                    </select><br>
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
                    <label fore="crea_entreprise"> Déclare avoir un projet de création ou de reprise
                    d'entreprise :</label>
                    <select name="crea_entreprise" id="crea_entreprise">
                        <option value="1">Oui</option>
                        <option value="0">Non</option>
                    </select><br>

                    <h2>Adresse</h2>
                    <label for="numero">Numéro:</label>
                    <input type="text" id="numero" name="numero"><br>
                    <label for="rue">Rue:</label>
                    <input type="text" id="rue" name="rue"><br>
                    <label for="complement">Complément:</label>
                    <input type="text" id="complement" name="complement"><br>
                    <label for="commune">Commune:</label>
                    <input type="text" id="commune" name="commune"><br>
                    <label for="telephone">Téléphone:</label>
                    <input type="text" id="telephone" name="telephone"><br>
                    <label for="courriel">Courriel:</label>
                    <input type="text" id="courriel" name="courriel"><br>
                    <label for="nationalite">Nationalité:</label>
                    <select id="nationalite" name="nationalite">
                        <option value="1">Français</option>
                        <option value="2">Européen</option>
                        <option value="3">Autre</option>
                    </select><br>

                    <h2>Représentant légal </h2>
                    <p>(à renseigner si l apprenti est mineur non émancipé)</p>
                    <label for="nom_legal">Nom:</label>
                    <input type="text" id="nom_legal" name="nom_legal"><br>
                    <label for="prenom_legal">Prénom:</label>
                    <input type="text" id="prenom_legal" name="prenom_legal"><br>

                    <label for="numero_r">Numéro:</label>
                    <input type="text" id="numero_r" name="numero"_r><br>
                    <label for="rue_r">Rue:</label>
                    <input type="text" id="rue_r" name="rue_r"><br>
                    <label for="complement_r">Complément:</label>
                    <input type="text" id="complement_r" name="complement_r"><br>
                    <label for="commune_r">Commune:</label>
                    <input type="text" id="commune_r" name="commune_r"><br>
                    <label for="telephone_r">Téléphone:</label>
                    <input type="text" id="telephone_r" name="telephone_r"><br>
                    <label for="courriel_r">Courriel:</label>
                    <input type="text" id="courriel_r" name="courriel_r"><br>
                    <button type="submit">Valider</button>
                </form>
            </body>
        </html>
    """

@router.post("/resultat")
def create_app(
    nom_naissance: str = Form(...),
    nom_usage: str = Form(...),
    prenom: str = Form(...),
    inscription_sportif_hn: bool = Form(...),
    nom_legal: str = Form("None"),
    prenom_legal: str = Form("None"),
    nationalite: int = Form(...),
    date_naissance: str = Form(...),
    sexe: str = Form(...),
    commune_naissance: str = Form(...),
    handicape: bool = Form(...),
    situation: int = Form(...),
    diplome: int = Form(...),
    classe: str = Form(...),
    intitule_diplome: str = Form(...),
    diplome_eleve: int = Form(...),
    crea_entreprise: bool = Form(...),

    numero: int = Form("None"),
    rue: str = Form(...),
    complement: str = Form("None"),
    commune: str = Form(...),
    telephone: str = Form(""),
    courriel: str = Form(""),

    rue_r: str = Form("None"),
    complement_r: str = Form("None"),
    commune_r: str = Form("None"),
    telephone_r: str = Form("None"),
    courriel_r: str = Form("None")
):
    identite = {
        "nom_naissance": nom_naissance,
        "nom_usage": nom_usage,
        "prenom": prenom,
        "nationalite": nationalite,
        "date_naissance": date_naissance,
        "sexe": sexe,
        "commune_naissance": commune_naissance,
        "inscription_sportif_hn": inscription_sportif_hn,
        "handicapé": handicape,
        "situation": situation,
        "diplome": diplome,
        "classe": classe,
        "intitule_diplome": intitule_diplome,
        "diplome_eleve": diplome_eleve,
        "crea_entreprise": crea_entreprise
    }
    representant_legal = {
        "nom": nom_legal,
        "prenom": prenom_legal,
        "rue": rue_r,
        "complement": complement_r,
        "commune": commune_r,
        "telephone": telephone_r,
        "courriel": courriel_r
    }
    adresse = {
        "numero": numero,
        "rue": rue,
        "complement": complement,
        "commune": commune,
        "telephone": telephone,
        "courriel": courriel
    }
    resultat = {
        "identite": identite,
        "representant_legal": representant_legal,
        "adresse": adresse
    }   
    return {"message": "Form data processed successfully"}