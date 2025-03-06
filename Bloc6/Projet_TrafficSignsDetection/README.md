# Bloc 6 : Direction de projets de gestion de données

## Projet : Traffic signs detection

## Problématique :
Déploiement d’applications d’IA embarquées sur des supports légers et/ou autonomes

## Objectif :
Déploiement de modèle de détection de panneaux de limitation de vitesse sur un Raspberry pi avec 2 impléméntations prototypes :
* Mini robot roulant
* Tableau de bord de voiture

## Implémentation :
/deploiment_mini_robot : modules de pilotage avec détection de panneaux du mini robot  
/deploy_tdb_voiture : modules détection de panneaux du boitier destiné au tdb de voiture
/modele_cnn_custom : modules de construction du modèle (approche 2)
                     detection de forme géométrisue
                     cnn "fait maison" : de decision "panneau ou non panneau"
                     cnn "fait maison" : de classification des panneaux
/modele_cnn_yolo : modules de cinstruction du modèle dérivé de "Yolo" par Transfert Learning
