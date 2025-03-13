## Elaboration du modèle "Custom" 

* rpi_traffic_signs_detector2v.py

Module de contrôle du Boitier avec 3 threads

* makeModel1.py

Entrainement du sous-modèle 1 de l'appeoche custom (Est-ce un panneau ?)

* makeModel2.py

Entrainement du sous-modèle 2 de l'appeoche custom (Classification des panneaux)

* makeNonPanneaux.py

Création de aléatoire de "non panneaux" pour l'entrainement du sous modèle 1

* data_prj.py

Fonctions partagées du projet  

* ./panneaux

Images des panneaux du périmètre de detection "brute"

* ./panneaux_diff

Images de panneaux hors périmètre "brute"