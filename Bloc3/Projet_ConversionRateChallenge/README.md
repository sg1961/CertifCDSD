# Bloc 3 : Analyse prédictive de données structurées par l'intelligence artificielle

## Projet : Conversion rate challenge

## Problématique :
* Comprendre et expliquer le comportement des utilisateurs qui visitent un site web
* Tenter de découvrir un nouveau levier d'action pour améliorer le taux de conversion du bulletin d'information 

## Objectif :
* Construire un modèle qui prédit si un utilisateur donné s'abonnera à la newsletter
* Analyser les paramètres du modèle pour mettre en évidence les caractéristiques importantes pour expliquer le comportement des utilisateurs 

## Implémentation :
* Conversion_rate_challenge_eda.ipynb

Analyse exploratoiredes des données - EDA

* Conversion_rate_challenge_modelA_countryMerge.ipynb

Approche 1 : Traitement ensemble des pays
Modèles : Logistic Regression, SVM, Decision Tree Classifier, Random Forest Classifier

* Conversion_rate_challenge_modelA_countrySplit.ipynb

Approche 2 : Traitement séparé des pays puis consolidation des prédictions
Modèles : Logistic Regression, SVM, Decision Tree Classifier, Random Forest Classifier

* Conversion_rate_challenge_model_best_V02B.ipynb

Entrairement du meilleur modèle sur l'ensemble du dataset et export pour soumission au challenge
(modele SVM, prédictions séparés par pays puis consolidation, Calibrage du meilleur seuil "proba" pour un meilleur f1-score)

* conversion_data_train.csv : data labelisée pour entrainement
* conversion_data_test.csv : data non labelisée pour sousmission des prédictions au challenge
