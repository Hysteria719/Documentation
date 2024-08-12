from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Now
class Departement(models.Model):
    nom = models.CharField(max_length=255,unique=True)
    description = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['nom']

class Photo(models.Model):
    nom = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    class Meta:
        ordering = ['nom']

class Utilisateur(AbstractUser):
    email = models.EmailField(verbose_name="adresse e-mail", max_length=255, unique=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class StatutRole(models.TextChoices):
        employe = 'employe'
        departement = 'departement'
        achat = 'achat'
        maintenance = 'maintenance'
        admin = 'admin'
    role = models.CharField(max_length=12, choices=StatutRole, default=StatutRole.employe)
    class Langue(models.TextChoices):
        fr = 'fr'
        eng = 'eng'
    langue = models.CharField(max_length=5,choices=Langue,default=Langue.fr)
    photo = models.ForeignKey(Photo, on_delete= models.CASCADE, null=True)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, null=True)

class ReinitialisationMotDePasse(models.Model):
    cree_le = models.DateTimeField(db_default = Now())
    token = models.CharField(max_length=255)    
    expire_le = models.DateTimeField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.CASCADE)
    class Meta:
        ordering = ['-cree_le']

class RefreshToken(models.Model):
    cree_le = models.DateTimeField(db_default = Now())
    token = models.CharField(max_length=255)    
    expire_le = models.DateTimeField()
    utilisateur = models.ForeignKey(Utilisateur, on_delete = models.CASCADE)
    class Meta:
        ordering = ['-cree_le']

class Notification(models.Model):
    message = models.TextField()
    date_envoi = models.DateTimeField(db_default=Now())
    class StatutNotif(models.TextChoices):
        envoye = 'envoye'
        non_envoye = 'non_envoye'
    statut = models.CharField(max_length=12,choices=StatutNotif,default=StatutNotif.non_envoye)

class NotifUtilisateur(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)

class Fournisseur(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    rue = models.CharField(max_length=255)
    num_rue = models.CharField(max_length=20)
    code_postal = models.CharField(max_length=20)
    ville = models.CharField(max_length=50)
    pays = models.CharField(max_length=20)
    class Meta:
        ordering = ['nom']

class Achat(models.Model):
    cree_le = models.DateTimeField(db_default = Now())
    num_facture = models.CharField(max_length=50, unique=True)
    date_achat = models.DateField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    utilisateur = models.ForeignKey(Utilisateur, on_delete= models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-cree_le']

class CategorieAppareil(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['nom']

class Appareil(models.Model):
    nom = models.CharField(max_length=50)
    num_serie = models.CharField(max_length=50, unique=True)
    reference = models.CharField(max_length=50)
    proch_maintenance = models.DateField()
    duree_garantie = models.DecimalField(max_digits=4, decimal_places=2)
    information = models.TextField(null=True, blank=True)
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE)
    categorie = models.ForeignKey(CategorieAppareil, on_delete=models.CASCADE)
    class Meta:
        ordering = ['nom']

class Document(models.Model):
    cree_le = models.DateTimeField(db_default = Now())
    nom = models.CharField(max_length=50)
    class TypeDocument(models.TextChoices):
        photo = 'photo'
        mode_emploi = 'mode_emploi'
        facture = 'facture'
    type = models.CharField(max_length=12, choices=TypeDocument)
    path = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    appareil = models.ForeignKey(Appareil, on_delete=models.CASCADE)

class Maintenance(models.Model):
    cree_le = models.DateTimeField(db_default= Now())
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    description = models.TextField()
    appareil = models.ForeignKey(Appareil, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-cree_le']

class Reservation(models.Model):
    cree_le = models.DateTimeField(db_default = Now())
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    class StatutReservation(models.TextChoices):
        en_attente = 'en_attente'
        accepte = 'accepte'
        refuse = 'refuse'
    statut = models.CharField(max_length=12, choices=StatutReservation, default=StatutReservation.en_attente)
    appareil = models.ForeignKey(Appareil, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-cree_le']

class HistoriqueAppareil(models.Model):
    cree_le = models.DateTimeField(db_default=Now())
    class StatutAppareil(models.TextChoices):
        entretien = 'entretien'
        occupe = 'occupe'
        libre = 'libre'
        detruit = 'detruit'
    statut = models.CharField(max_length=10, choices=StatutAppareil, default=StatutAppareil.libre)
    appareil = models.ForeignKey(Appareil, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-cree_le']