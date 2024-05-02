## pour chaque partie il faut importer ici j'ai mis Utilisateur, voir models.py
    >>> from NomApp.models import Utilisateur

## Créer un utilisateur avec un password hashé    
    >>> user = Utilisateur.objects.create_user("fab", "fab@aa.com", "Azertyuiop$1qsdf")
    >>> user.save()

## Modifier le mot de passe utilisateur et qu'il soit hashé    
    >>> u = User.objects.get(username="john")
    >>> u.set_password("new password")
    >>> u.save()    
