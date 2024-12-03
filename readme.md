Comment lancer la partie Back-End et le Front-End : 

Première étape : Lancer docker 
Utilisant PostgreSQL on passe par docker pour pouvoir lancer tout simplement la base de donnée.

Seconde étape : 
Une fois la base de donnée lancer tapez la commande :  uvicorn app.main:app --reload 

Dernière étape : 
Une fois le back et la base de donnée lancer, il suffira de taper la commande au niveau du front-end : npm run dev

Pour accéder aux données de la bdd : 
1- Lancer le CMD 
2- Aller sur le repo du back-end. Par exemple : c:\user\utilisateur\cerfa\cerfabackend
3- Taper : docker exec -it nom-de-la-bdd(docker) psql -U nom-utilisateur  par exemple pour moi ça donne : docker exec -it cerfabackend-postgres-1 psql -U noa 
4- Se connecter à la bonne base de donnée avec \c pour \connect le-nom-de-la-bdd. Si vous ne connaissez pas le nom vous pouvez taper \l qui équivaut à \list afin de voir toute les bases de données
5- Une fois connecter à la bdd, il vous restera plus qu'à faire vos requêtes à la main. Pour voir toutes les tables, vous pouvez taper \dt 