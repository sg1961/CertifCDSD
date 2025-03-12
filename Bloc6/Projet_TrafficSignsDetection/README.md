# (Bloc 6) Projet : Traffic signs detection

## Problématique :
Déploiement d’applications d’IA embarquées sur des supports légers et/ou autonomes

## Objectif :
Déploiement de modèle de détection de panneaux de limitation de vitesse sur un Raspberry pi avec 2 impléméntations prototypes :
* Mini robot roulant
* Tableau de bord de voiture

## Implémentation :

* ./modele_cnn_yolo

(approche 1 - transfert learning) modules de construction du modèle dérivé de "Yolo"

* ./modele_cnn_custom
  
(approche 2 - fait maison) modules de construction du modèle :
(detection de forme géométrisue + cnn de decision "panneau ou non panneau" + cnn de classification des panneaux

* ./perf_bench

modules et ihm streamlit de bench des modèles

* ./deploiment_mini_robot

Déploiment des modules de pilotage avec détection de panneaux du mini robot

* ./deploy_tdb_voiture
  
Déploiement des modules détection de panneaux du boitier destiné au tdb de voiture



