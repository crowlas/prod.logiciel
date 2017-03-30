TP #2
==============================================================================================
**VOUS VOUS METTREZ EN BINOME POUR LA SUITE DU TP**

## Données d'Installations Sportives des Pays de la Loire
1. telecharger les 3 fichiers CSV jeux de données, au format CSV : 
    * [Installations]
  http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations
    * [Equipements]
  http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-equipements
  	* [Activités]
  http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-activites-des-fiches-equ

2. manipuler les fichiers CSV comme au TP #1 avec le module 'csv'

## Base de Données  :  mettre en place une base de données alimentée par ces fichiers de données équipement, activités, installations
1. Définir la structure de BD (avec clés primaires & clés étrangères), en fonction de l'API
2. charger les données d'EQUIPEMENTS et d'ACTIVITES en CSV, et alimenter la BD
3. charger les données d'INSTALLATIONS en CSV ou JSON (au choix), et alimenter la BD
> RQ : vous pouvez installer MySQL connector pour python (http://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html),
> ou sinon utiliser sqlite qui est supporté nativement par Python (pour accéder à la base, utiliser par exemple l'outil www.sqllitebrowser.org ou le plugin SQLlite manager de firefox)

## Structure des données en objet
A partir d'une requête à la BD par exemple
=> construire une structure d'objets (grappe d'objets) qui représente ces données objets qui peuvent être manipulés ensuite en objets

## Recherche
Faire évoluer votre application pour afficher des données filtrées des équipements sportifs (avec une recherche sur certaines données que l'utilisateur sélectionnera), par ex : pouvoir afficher les lieux & salles correspondant à un sport donné

