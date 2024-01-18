# Créez un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
.\venv\Scripts\activate

# Desactiver l'environnement (quitter)
deactivate

# Installez dépendances Django (dans venv)
pip install -r requirements.txt

# Appliquez les migration Django
python manage.py migrate


# Lancez le serveur de développement
python manage.py runserver