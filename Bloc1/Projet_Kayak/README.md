# (Bloc 1) Projet : Kayak

## Problématique :
l’équipe Kayak a découvert que 70% de leurs utilisateurs qui planifient un voyage aimeraient avoir plus d’informations sur la destination ou ils vont 

## Objectif :
Créer une application pour les utilisateurs Kayak de recommandation :
* des meilleures destinations (au sens météo)
* des meilleurs hôtels de ces destinations (au sens notation booking.com)

## Présentation du projet

* Bloc1_Projet_Kayak-Presentation.pptx

## Implémentation :

* kayak_get_geoloc_and_weather.ipynb

Module de récupération (via APIs) des informations de localisation des villes et des informations méteo

* kayak_get_hotels.py & kayak_run_scraping_hotels

Module de récupération des informations sur les hotels (par sraping) depuis le site de booking.com

* kayak_pull_data_to_s3.ipynb

Module d'enregistrement des données brutes (villes, localisations et hotels) sur AWS : S3

* kayak_pull_data_to_db.ipynb

Module d'enregistrement des données structurées (villes et hotels) en base de données Postgres sur AWS

* kayak_maps.ipynb

Module de production des cartes des meilleurs destinations et des meilleurs hotels par destination

* kayak_secret.py (non présent sur GitHub)

Module contenant les informations pour acceder aux stockages AWS : S3 et DB Postgres
