from datetime import timezone
from django.db import models
from django.core.files.storage import FileSystemStorage
from accounts.models import Utilisateur

# Create your models here.
class Statutannees(models.Model):
    Statutannee = models.CharField(max_length=50,null=False)
    def __str__(self):
        return f'{self.Statutannee}'
    
class Statutdecoups(models.Model):
    Statutdecoup = models.CharField(max_length=50,null=False)
    def __str__(self):
        return f'{self.Statutdecoup}'
    
class Anneescolaires(models.Model):
    Anneescolaire = models.CharField(max_length=10,null=False)
    Statutannee = models.ForeignKey(Statutannees, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.Anneescolaire}'

class Genres(models.Model):
    Sexe = models.CharField(max_length=10)
    def __str__(self):
        return f'{self.Sexe}'

class Matrimoniales(models.Model):
    Matrimoniale = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Matrimoniale}'

class Typeecoles(models.Model):
    Typeecole = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Typeecole}'

class Statuts(models.Model):
    Statut = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Statut}'

class Typematieres(models.Model):
    Typematiere = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Typematiere}'

class Niveaux(models.Model):
    Niveauetude = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Niveauetude}'



class Ecoles(models.Model):
    Etablissement = models.CharField(max_length=250)
    Ville = models.CharField(max_length=50,null=True)
    Telephone = models.CharField(max_length=15,null=True)
    Contact = models.CharField(max_length=15,null=True)
    Adresse = models.CharField(max_length=50,null=True)
    Natureecole = models.ForeignKey(Typeecoles, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images/Photos/ecole',null=True)
    def __str__(self):
        return f'{self.Etablissement}'

fs = FileSystemStorage(location='/media/photos')
class Enseignants(models.Model):
    Matricule = models.CharField(max_length=100,null=True,unique=True)
    Nom = models.CharField(max_length=100)
    Prenoms = models.CharField(max_length=250)
    Datenaissance = models.DateField(null=True)
    Lieunaissance = models.CharField(max_length=15,null=True)
    Telephone = models.CharField(max_length=15,null=True)
    Contact = models.CharField(max_length=15,null=True)
    Email = models.CharField(max_length=50,null=True)
    Photo = models.ImageField(upload_to='Images/Photos/enseignants',null=True, blank=True)
    Ecole = models.ForeignKey(Ecoles, on_delete=models.CASCADE)
    Sexe = models.ForeignKey(Genres, on_delete=models.CASCADE)
    Statut = models.ForeignKey(Statuts, on_delete=models.CASCADE)
    User = models.OneToOneField(Utilisateur, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.Nom} {self.Prenoms}"


class Salles(models.Model):
    Salle = models.CharField(max_length=50)
    Nbreplace = models.IntegerField()
    Effectif = models.IntegerField(null=True)
    Niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    Etablissement = models.ForeignKey(Ecoles, on_delete=models.CASCADE)
    Anneescolaire = models.ForeignKey(Anneescolaires, on_delete=models.CASCADE,null=True)
    Professeurprincipal = models.ForeignKey(Enseignants, on_delete=models.CASCADE,null=True)
    Planning = models.ImageField(upload_to='Images/Photos/salles',null=True, blank=True)
    def __str__(self):
        return f'{self.Salle}'
    
class Matieres(models.Model):
    Matiere = models.CharField(max_length=50)
    Typematiere = models.ForeignKey(Typematieres, on_delete=models.CASCADE)
    Professeur = models.ForeignKey(Enseignants, on_delete=models.CASCADE,null=True)
    Salle = models.ForeignKey(Salles, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.Matiere}'
    

class Decoupages(models.Model):
    Decoupage = models.CharField(max_length=10,null=False)
    Statutdecoup = models.ForeignKey(Statutdecoups, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.Decoupage}'   

    
class Etudiants(models.Model):
    Matricule = models.CharField(max_length=10,null=True,unique=True)
    Nom = models.CharField(max_length=100)
    Prenoms = models.CharField(max_length=250)
    Datenaissance = models.DateField(null=True)
    Lieunaissance = models.CharField(max_length=15,null=True)
    Telephone = models.CharField(max_length=15,null=True)
    Contact = models.CharField(max_length=15,null=True)
    Email = models.CharField(max_length=50,null=True)
    Photo = models.ImageField(upload_to='Images/Photos/etudiants',null=True)
    Ecole = models.ForeignKey(Ecoles, on_delete=models.CASCADE)
    Sexe = models.ForeignKey(Genres, on_delete=models.CASCADE)
    Matrimoniale = models.ForeignKey(Matrimoniales, on_delete=models.CASCADE,null=True)
    Niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    Salle = models.ForeignKey(Salles, on_delete=models.CASCADE)
    User = models.OneToOneField(Utilisateur, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.Nom} {self.Prenoms}"


class DossierScolaires(models.Model):
    Anneescolaire = models.ForeignKey(Anneescolaires, on_delete=models.CASCADE, null=True)
    Etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE, related_name='dossiers_scolaires', null=True)
    HeuresabsenceS1 = models.IntegerField(default=0)
    HeuresabsenceS2 = models.IntegerField(default=0)
    Matricule = models.CharField(max_length=50, null=True)
    Nom = models.CharField(max_length=100, null=True)
    Prenoms = models.CharField(max_length=100, null=True)
    Datenaissance = models.DateField( null=True)
    Lieunaissance = models.CharField(max_length=100, null=True)
    Telephone = models.CharField(max_length=15, null=True)
    Contact = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=100, null=True)
    Photo = models.ImageField(upload_to='Images/Photos', null=True, blank=True)
    Ecole = models.ForeignKey(Ecoles, on_delete=models.CASCADE, null=True)
    Sexe = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)
    Matrimoniale = models.ForeignKey(Matrimoniales, on_delete=models.CASCADE, null=True)
    Niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE, null=True)
    Salle = models.ForeignKey(Salles, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.Nom} {self.Prenoms}'

    
class DossierFinances(models.Model):
    Anneescolaire = models.ForeignKey(Anneescolaires, on_delete=models.CASCADE, null=True)
    Etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE, related_name='dossiers_finances', null=True)
    Montantscolarit = models.IntegerField(null=True)
    Montantvers = models.IntegerField(null=True)
    Montantrestant = models.IntegerField(null=True)
    Matricule = models.CharField(max_length=50, null=True)
    Nom = models.CharField(max_length=100, null=True)
    Ecole = models.ForeignKey(Ecoles, on_delete=models.CASCADE, null=True)
    Sexe = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)
    Niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE, null=True)
    Salle = models.ForeignKey(Salles, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.Nom}'

class HistoriquesVers(models.Model):
    Etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    Anneescolaire = models.ForeignKey(Anneescolaires, on_delete=models.CASCADE)
    Datevers = models.DateField(null=True)
    Montantscolarit = models.IntegerField(null=True)
    Montantvers = models.IntegerField(null=True)
    Montantrestant = models.IntegerField(null=True)
    Montantvers = models.IntegerField(null=True)
    Nom = models.CharField(max_length=100, null=True)
    Ecole = models.ForeignKey(Ecoles, on_delete=models.CASCADE, null=True)
    Sexe = models.ForeignKey(Genres, on_delete=models.CASCADE, null=True)
    Niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE, null=True)
    Salle = models.ForeignKey(Salles, on_delete=models.CASCADE, null=True)
    Dossierfinance = models.ForeignKey(DossierFinances, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.Nom} {self.Dossierfinance}'

class HistoriquesAbs(models.Model):
    Etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    Anneescolaire = models.ForeignKey(Anneescolaires, on_delete=models.CASCADE)
    Decoupage = models.ForeignKey(Decoupages, on_delete=models.CASCADE,null=True)
    Cours = models.ForeignKey(Matieres, on_delete=models.CASCADE)
    Heuredebut = models.TimeField()
    Heurefin = models.TimeField()
    Datecours = models.DateField(null=True)

    def __str__(self):
        return f"Dossier scolaire de {self.Etudiant} - {self.Anneescolaire}"

class Catalogues(models.Model):
    Nom = models.CharField(max_length=250)
    Prix = models.IntegerField(null=True)
    Niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)

class Moyennes(models.Model):
    Etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    Decoupage = models.ForeignKey(Decoupages, on_delete=models.CASCADE,null=True)
    Anneescolaire = models.ForeignKey(Anneescolaires, on_delete=models.CASCADE,null=True)
    Moyenne = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    Total = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    Rang = models.CharField(max_length=15,null=True)
    def __str__(self):
        return f"{self.Etudiant}"
    
class Notes(models.Model):
    Etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    Decoupage = models.ForeignKey(Decoupages, on_delete=models.CASCADE,null=True)
    Anneescolaire = models.ForeignKey(Anneescolaires, on_delete=models.CASCADE,null=True)
    Cours = models.ForeignKey(Matieres, on_delete=models.CASCADE)
    Note = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    Salle = models.ForeignKey(Salles, on_delete=models.CASCADE,null=True)
    Appreciation = models.CharField(max_length=50,null=True)
    Typematiere = models.ForeignKey(Typematieres, on_delete=models.CASCADE,null=True)
    Professeur = models.ForeignKey(Enseignants, on_delete=models.CASCADE,null=True)


class Contacturgences(models.Model):
    Qualite = models.CharField(max_length=100,null=True)
    Nom = models.CharField(max_length=100,null=True)
    Prenoms = models.CharField(max_length=250,null=True)
    Etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    Telephone = models.CharField(max_length=15,null=True)
    Contact = models.CharField(max_length=15,null=True)
    Email = models.CharField(max_length=50,null=True)
    

class Documents(models.Model):
    Title = models.CharField(max_length=255)
    File = models.FileField(upload_to='Documents/Pedagogie/Cours')
    Salle = models.ForeignKey(Salles, on_delete=models.CASCADE,null=True)
    Anneescolaire = models.ForeignKey(Anneescolaires, on_delete=models.CASCADE,null=True)
    Cours = models.ForeignKey(Matieres, on_delete=models.CASCADE)
    Typematiere = models.ForeignKey(Typematieres, on_delete=models.CASCADE,null=True)
 
class Services(models.Model):
    Service = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Service}'

class Postes(models.Model):
    Poste = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Poste}'

class Avis(models.Model):
    Aviss = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Aviss}'
    
class Messages(models.Model):
    nom = models.CharField(max_length=100)
    Etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    Salle = models.ForeignKey(Salles, on_delete=models.CASCADE)
    sujet = models.CharField(max_length=100)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sujet
    
class Messagess(models.Model):
    nom = models.CharField(max_length=100,null=True)
    Enseignant = models.ForeignKey(Enseignants, on_delete=models.CASCADE,null=True)
    Ecole = models.ForeignKey(Ecoles, on_delete=models.CASCADE,null=True)
    sujet = models.CharField(max_length=100,null=True)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sujet

class Personnels(models.Model):
    Service = models.ForeignKey(Services, on_delete=models.CASCADE)
    Poste = models.ForeignKey(Postes, on_delete=models.CASCADE)
    Matricule = models.CharField(max_length=10,null=True,unique=True)
    Nom = models.CharField(max_length=100)
    Prenoms = models.CharField(max_length=250)
    Sexe = models.ForeignKey(Genres, on_delete=models.CASCADE,null=True)
    Matrimoniale = models.ForeignKey(Matrimoniales, on_delete=models.CASCADE,null=True)
    Datenaissance = models.DateField(null=True)
    Lieunaissance = models.CharField(max_length=15,null=True)
    Telephone = models.CharField(max_length=15,null=True)
    Contact = models.CharField(max_length=15,null=True)
    Email = models.CharField(max_length=50,null=True)
    Photo = models.ImageField(upload_to='Images/Photos/personnels',null=True)
    Statut = models.CharField(max_length=15,null=True)
    def __str__(self):
        return f"{self.Nom} {self.Prenoms}"

class Autorisationsauditeur(models.Model):
    Etudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    Salle = models.ForeignKey(Salles, on_delete=models.CASCADE,null=True)
    Contact = models.CharField(max_length=15,null=True)
    Periode = models.DecimalField(max_digits=4, decimal_places=1,null=True)
    Datedebut = models.DateField(null=True)
    Heuredebut = models.TimeField()
    Datefin = models.DateField(null=True)
    Heurefin = models.TimeField()
    Motif = models.CharField(max_length=1000,null=True)
    Datereprise = models.DateField(null=True)
    Heurereprise = models.TimeField()
    Remplacant = models.CharField(max_length=250,null=True)
    Contactremplacant = models.CharField(max_length=15,null=True)
    Aviss = models.ForeignKey(Avis, on_delete=models.CASCADE)

class Autorisationspersonnel(models.Model):
    Personnel = models.ForeignKey(Personnels, on_delete=models.CASCADE)
    Service = models.ForeignKey(Services, on_delete=models.CASCADE)
    Poste = models.ForeignKey(Postes, on_delete=models.CASCADE)
    Contact = models.CharField(max_length=15,null=True)
    Periode = models.DecimalField(max_digits=4, decimal_places=1,null=True)
    Datedebut = models.DateField(null=True)
    Heuredebut = models.TimeField()
    Datefin = models.DateField(null=True)
    Heurefin = models.TimeField()
    Motif = models.CharField(max_length=1000,null=True)
    Datereprise = models.DateField(null=True)
    Heurereprise = models.TimeField()
    Remplacant = models.CharField(max_length=250,null=True)
    Contactremplacant = models.CharField(max_length=15,null=True)
    Aviss = models.ForeignKey(Avis, on_delete=models.CASCADE)

class Autorisationsenseignant(models.Model):
    Enseignant = models.ForeignKey(Enseignants, on_delete=models.CASCADE)
    Ecole = models.ForeignKey(Ecoles, on_delete=models.CASCADE,null=True)
    Contact = models.CharField(max_length=15,null=True)
    Periode = models.DecimalField(max_digits=4, decimal_places=1,null=True)
    Datedebut = models.DateField(null=True)
    Heuredebut = models.TimeField()
    Datefin = models.DateField(null=True)
    Heurefin = models.TimeField()
    Motif = models.CharField(max_length=1000,null=True)
    Datereprise = models.DateField(null=True)
    Heurereprise = models.TimeField()
    Remplacant = models.CharField(max_length=250,null=True)
    Contactremplacant = models.CharField(max_length=15,null=True)
    Aviss = models.ForeignKey(Avis, on_delete=models.CASCADE)

class Missions(models.Model):
    Personnel = models.ForeignKey(Personnels, on_delete=models.CASCADE)
    Service = models.ForeignKey(Services, on_delete=models.CASCADE)
    Poste = models.ForeignKey(Postes, on_delete=models.CASCADE)
    Lieumission = models.CharField(max_length=250,null=True)
    Mission = models.CharField(max_length=1000,null=True)
    Datedebut = models.DateField(null=True)
    Datefin = models.DateField(null=True)
    Delegation = models.CharField(max_length=1000,null=True)
    Moyen = models.CharField(max_length=250,null=True)
    Datemission = models.DateField(null=True)
    Aviss = models.ForeignKey(Avis, on_delete=models.CASCADE)

class License(models.Model):
    license_code = models.CharField(max_length=100)
    activation_date = models.DateField()
    expiration_date = models.DateField()
    # Autres champs de licence

    def is_valid(self):
        return self.expiration_date >= timezone.now().date() # type: ignore
    