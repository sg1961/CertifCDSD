# (Bloc 6) Projet : Traffic signs detection

## Problématique :
Déploiement d’applications d’IA embarquées sur des supports légers et/ou autonomes

## Objectif :
Déploiement de modèle de détection de panneaux de limitation de vitesse sur un Raspberry pi avec 2 impléméntations prototypes :
* Mini robot roulant
* Tableau de bord de voiture

## Implémentation :

* ./modele_cnn_yolo

(approche 1 - modèle via transfer learning) modules de construction du modèle dérivé de "Yolo"

* ./modele_cnn_custom
  
(approche 2 - modèle fait maison) modules de construction d'un modèle "custom" de détection de panneaux :
Principe : Detection de formes géométriques + 1 cnn de décision "panneau ou non panneau" + 1 cnn de classification des panneaux

* ./perf_bench

Modules et ihm streamlit de mesure des performances des modèles

* ./deploiment_mini_robot

Déploiment des modules de pilotage avec détection de panneaux du mini robot roulant

* ./deploy_tdb_voiture
  
Déploiement des modules de détection de panneaux sur un boitier destiné au tableau de bord de voiture



