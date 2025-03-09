# (Bloc 5) Projet : GetAround

## Problématique :
Getaround projette de :
* mettre en place un délai minimum entre 2 locations pour mieux respecter le début des locations et réduire de potentielles insatisfactions clients.
* Pouvoir suggérer des prix optimaux pour les propriétaires de voitures 

## Objectif :
* Mise eu point et déploiement d’un tableau pour aider Gettaround à prendre les bonnes décisions  pour optimiser la mise la mise en œuvre de ce délai minimun (impacts, cible, calibrage, …)
* Mise au point d’un modèle de prédiction et déploiement d’une API de proposition de prix de location.

## Présentation du projet :
* Bloc5_Getaround.pptx

## Implémentation :

* get_around_delay_analysis.ipynb

Exploration, nettoyage et préparation des données

Production de restitutions d'analyses des impacts de mise en oeuvre de délai entre 2 locations

* get_around_pricing_project.ipynb

Exploration, nettoyage et préparation des données

Elaboration de modèle de proposition de prix : (modèle base de Régression linéaire, Ridge et Lasso)

* ./model

Différentes variantes de modèles testés

* ./get_around_pricing_deploy
  
Déploiement d'API de publication des propositions de prix de courses Uber
Lien : https://sg1961-get-around-api.hf.space

* ./get_around_tdb_deploy
  
Déploiement de "tableau de bord - streallit" de publication d'nalyses des courses Uber
Lien :  https://sg1961-getaround.hf.space

* get_around_delay_analysis.xls
  
Données sources - (courses Ubers)

* get_around_pricing_project.csv
  
Données sources - (prix des courses Ubers)
