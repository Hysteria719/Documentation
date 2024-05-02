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
- git branch

## Changer de branche 
- git checkout main

## Changer d'utilisateur en local
        git config --local user.name "VotreNomUtilisateur"
        git config --local user.email "votre@email.com"

## push avec token
        git remote set-url origin https://USERNAME:TOKEN@github.com/Hysteria719/Documentation.git
        git push origin main 

## Problème 
        git config --global credential.helper store
        git credential approve
        git push https://USERNAME:TOKEN@github.com/USERNAME/REPO.git

