## Créer un utilisateur avec un password hashé
    from NomApp.models import Utilisateur
    user = Utilisateur.objects.create_user("fab", "fab@aa.com", "Azertyuiop$1qsdf")
    user.save()