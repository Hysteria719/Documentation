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

## Installez merchex si besoin vérifie si le dossier merchex existe
- django-admin startproject merchex
# Si projet existe déjà
## Installez dépendances Django si le projet existe déjà (dans venv)
- pip install -r requirements.txt

## Appliquez les migration Django
- python manage.py migrate

# Lancer serveur
## Lancez le serveur de développement
- python manage.py runserver