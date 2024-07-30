# Lorsqu'on doit ajouter des données contenant des dates avec l'heure faut spécifier le fuseau horaire avec postgressql Django
## Exemple de code pour l'ajout d'un achat d'appareil
    >>> from django.utils import timezone
    >>> from datetime import datetime
    >>> aware_datetime = timezone.make_aware(datetime(2024,1,10,10,0,0))
    
    >>> anne = Utilisateur.objects.get(username='anne')  
    >>> fourn = Fournisseur.objects.get(nom='Techmeasure') 
    >>> achat = Achat.objects.create(
    ... cree_le=aware_datetime, num_facture='FAC20240110', date_achat='2024-01-10', prix=1200.50,        
    ... utilisateur=anne,fournisseur=fourn)                                                      
    >>> achat.save()
