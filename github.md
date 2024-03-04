## Si pas dépot
- git init
## 
- git clone
- git add .
- git commit -m "MESSAGE"

## Poussez les modification vers le dépôt distant (GitHub)
- git push origin main

## Récupérez les dernières modifications du dépot distant
- git pull origin main

## Vérifier dans quelle branche et autre info
- git status

## Changer de branche 
- git checkout main

## Problème 
        git config --global credential.helper store
        git credential approve
        git push https://USERNAME:TOKEN@github.com/USERNAME/REPO.git