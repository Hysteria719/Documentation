## Installation de django-cors-headers
- pip install django-cors-headers

## Ajout l'app dans setting.py
- INSTALLED_APPS = [ 'corsheaders', ]

## Ajout MIDDLEWARE dans setting.py
- MIDDLEWARE = [ 'corsheaders.middleware.CorsMiddleware', ]

## Ajouter CORS_ALLOWED_ORIGINS = [] dans setting.py
- CORS_ALLOWED_ORIGINS = [ "http://localhost:5173", ]