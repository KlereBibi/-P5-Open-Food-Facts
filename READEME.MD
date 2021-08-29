# Utilisez les données publiques de l'OpenFoodFacts 

*L'application consiste à récupérer les données de l'openfoodfact, les enregistrer dans notre propre base de donnée afin de rechercher des substituts dans une liste de produits*

## Pour commencer

### Pré-requis

Ce qu'il est requis pour commencer...

* Un Système d'exploitation (ici Windows 10 Famille utilisé)
* Python 3 *https://www.python.org/downloads/* - version utilisé : 3.9.1
* Git *https://git-scm.com/downloads* - version utilisé : 2.33.0
* Un compte GitHub *https://github.com/* 
* Un éditeur de code (ici VS CODE est utilisé *https://code.visualstudio.com/download*)
* MySQL *https://dev.mysql.com/downloads/mysql/* 
    -> Exemple de tutoriel pour installation MySQL sur Windows10 *https://www.youtube.com/watch?v=K1SOagDC3Xg*

### Installation

* Dans votre terminal, clonez le package avec git sur votre dépôt local (ordinateur) comme ceci:
 - Etape 1 : initialisation de git dans le dossier correspondant avec: *git init*
 - Etape 2: *git remote add <nom du fichier> https://github.com/KlereBibi/-P5-Open-Food-Facts.git* 
 - Etape 3: *git clone https://github.com/KlereBibi/-P5-Open-Food-Facts.git* 
* Toujours dans le terminal, initialiser votre environnement virtuel:
 - Etape 1: installation de pipenv avec la commande: *pip install pipenv*
 - Etape 2: initialisation de l'environnement virtuel dans le package: *pipenv shell* 
 - Etape 3: installer les modules nécessaires grâce au fichier requierements.txt: *pipenv install -r requirements.txt*

## Création de la base de donnée MySQL

- Ouvrez votre terminal et tappez la commande : *mysql -h localhost -u root -p*
- Tappez le mot de passe MySQL que vous avez inscrit lors de l'installation de MySQL
- Tappez la commande : *CREATE DATABASE (nom de la base de donnée) CHARACTER SET 'utf8mb4'*;
- Allez dans models et settings 
- Ouvrez le fichier setting 
- Modifiez PASSWORD = "(*votre mot de passe*)" DATABASE = "(*nom de votre base de donnée*)"

## Démarrage
* Ouvrez le fichier *main.py* avec votre éditeur de code
* Pour VS CODE, appuyez sur F5 pour lancer le fichier dans le terminal
* Pour les autres éditeurs de texte, lancer votre programme 
* Veuillez suivre les indications de l'application 

## Fabriqué avec
* VS CODE - Editeur de texte

## Versions

* Windows 10 Famille - Système d’exploitation 64 bits 
* python 3.9.1
* git version 2.33.0.windows.1
* MySQL version  8.0.25

## Auteur
Claire Biedermann
