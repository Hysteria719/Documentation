# D'abord
## Créez un environnement virtuel
- python -m venv venv

## Activer l'environnement virtuel
- .\venv\Scripts\activate

## Desactiver l'environnement (quitter)
- deactivate


# Si nouveau projet
## Installez django (dans venv)
- pip install django

## Ajouter les dépendance dans le fichier requirement
- pip freeze > requirements.txt

## Créer un nouveau Projet (le squelette du projet )
- django-admin startproject NomProjet

## Créer une nouvelle application (Utilisé à l'intérieur d'un projet)
- python manage.py startapp NomApp

# Si projet existe déjà
## Installez dépendances Django si le projet existe déjà (dans venv)
- pip install -r requirements.txt

## Appliquez les migration Django
- python manage.py migrate


# Lors de la modification de la db model
## Créez une nouvelle migration
- python manage.py makemigrations
## Appliquez les migrations
- python manage.py migrate


# Créer une nouvelle application
- python manage.py startapp NomApp


# Lancer serveur
## Lancez le serveur de développement
- python manage.py runserver