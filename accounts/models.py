from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utilisateur(AbstractUser):
    
    ETUDIANT = 'ETUDIANT'
    ENSEIGNANT = 'ENSEIGNANT'
    GESTIONNAIRE = 'GESTIONNAIRE'
    ACADEMIQUE = 'ACADEMIQUE'
    DIRECTION = 'DIRECTION'
    ADMINISTRATEUR = 'ADMINISTRATEUR'
    ADMINISTRATEURSUPER = 'ADMINISTRATEURSUPER'
    
    ROLE_CHOICES = (
        (GESTIONNAIRE, 'Gestionnaire'),
        (ENSEIGNANT, 'Enseignant'),
        (ETUDIANT, 'Etudiant'),
        (ADMINISTRATEUR, 'Administrateur'),
        (ADMINISTRATEURSUPER, 'Administrateur Super'),
        (DIRECTION, 'Direction Institution'),
        (ACADEMIQUE, 'Direction Academique'),
    )
    profile_photo = models.ImageField(verbose_name='photo de profil',upload_to='Images/Photos/utilisateurs',null=True, blank=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='rôle')
    statut = models.CharField(max_length=10,null=True)