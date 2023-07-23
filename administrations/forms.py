from django.core import validators
from django import forms
from django.forms import DateTimeField
from .models import Etudiants,Notes,Matieres,Messages,Messagess
from .models import Ecoles,Niveaux,HistoriquesAbs
from .models import Salles,Matieres,Decoupages,Personnels,Services,Postes,Autorisationsauditeur,Autorisationsenseignant,Autorisationspersonnel,Avis,Missions
from .models import Enseignants, Anneescolaires,Documents,Typeecoles,Typematieres,Catalogues
from django.forms.widgets import SelectDateWidget


class EtudiantRegistration(forms.ModelForm):
    class Meta:
        model = Etudiants
        fields = ['Matricule','Nom', 'Prenoms','Datenaissance','Lieunaissance','Telephone','Contact','Email','Ecole','Sexe','Niveau','Salle', 'Photo','Matrimoniale']
        widgets = {
            'Matricule':forms.TextInput(attrs={'class':'form-control','placeholder': 'Matricule'} ),
            'Nom':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Prenoms':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Lieunaissance':forms.TextInput(attrs={'class':'form-control'} ),
            'Sexe' : forms.Select(attrs={'class':'form-select'} ),
            'Ecole' : forms.Select(attrs={'class':'form-select'} ),
            'Niveau' : forms.Select(attrs={'class':'form-select'} ),
            'Salle' : forms.Select(attrs={'class':'form-select'} ),
            'Telephone':forms.TextInput(attrs={'class':'form-control','placeholder': 'Telephone'} ),
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact'} ),
            'Datenaissance':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Email':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Photo': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            'Matrimoniale': forms.Select(attrs={'class':'form-select'} ),
            } 

class EtudiantclasseRegistration(forms.ModelForm):
    class Meta:
        model = Etudiants
        fields = ['Matricule','Nom','Ecole','Sexe','Niveau', 'Prenoms','Datenaissance','Lieunaissance','Telephone','Contact','Email','Ecole','Sexe','Niveau','Salle', 'Photo','Matrimoniale']
        widgets = {
            'Matricule':forms.TextInput(attrs={'class':'form-control','placeholder': 'Matricule'} ),
            'Nom':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Prenoms':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Lieunaissance':forms.TextInput(attrs={'class':'form-control'} ),
            'Sexe' : forms.Select(attrs={'class':'form-select'} ),
            'Telephone':forms.TextInput(attrs={'class':'form-control','placeholder': 'Telephone'} ),
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact'} ),
            'Datenaissance':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Email':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Photo': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            'Matrimoniale': forms.Select(attrs={'class':'form-select'} ),

            'Ecole' : forms.Select(attrs={'class':'form-select'} ),
            'Niveau' : forms.Select(attrs={'class':'form-select'} ),
            'Salle' : forms.Select(attrs={'class':'form-select'} ),
            } 

class EtudiantmRegistration(forms.ModelForm):
    class Meta:
        model = Etudiants
        fields = ['Matricule','Nom', 'Prenoms','Datenaissance','Lieunaissance','Telephone','Contact','Email','Sexe','Niveau','Salle', 'Photo','Matrimoniale','Ecole']
        widgets = {
            'Matricule':forms.TextInput(attrs={'class':'form-control','placeholder': 'Matricule'} ),
            'Nom':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Prenoms':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Lieunaissance':forms.TextInput(attrs={'class':'form-control'} ),
            'Sexe' : forms.Select(attrs={'class':'form-select'} ),
            'Niveau' : forms.Select(attrs={'class':'form-select niveau-select'} ),  # Ajouter la classe CSS 'niveau-select' ici
            'Salle' : forms.Select(attrs={'class':'form-select salle-select'} ),  # Ajouter la classe CSS 'salle-select' ici
            'Telephone':forms.TextInput(attrs={'class':'form-control','placeholder': 'Telephone'} ),
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact'} ),
            'Datenaissance':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Email':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Photo': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            'Matrimoniale': forms.Select(attrs={'class':'form-select'} ),
            'Ecole' : forms.Select(attrs={'class':'form-select'} ),
        } 

    def __init__(self, *args, **kwargs):
        super(EtudiantmRegistration, self).__init__(*args, **kwargs)
        self.fields['Salle'].queryset = Salles.objects.none()

        if 'Niveau' in self.data:
            try:
                niveau_id = int(self.data['Niveau'])
                self.fields['Salle'].queryset = Salles.objects.filter(Niveau__id=niveau_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['Salle'].queryset = self.instance.Niveau.salles_set.all()








        

class EcoleRegistration(forms.ModelForm):
    class Meta:
        model = Ecoles
        fields = ['Etablissement', 'Ville','Natureecole','Telephone','Contact','Adresse','image']
        widgets = {
            'Etablissement':forms.TextInput(attrs={'class':'form-control','placeholder': 'Institution'} ),
            'Ville':forms.TextInput(attrs={'class':'form-control','placeholder': 'Ville'} ),
            'Natureecole' : forms.Select(attrs={'class':'form-select'} ),
            'Telephone':forms.TextInput(attrs={'class':'form-control','placeholder': 'Telephone'} ),
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact'} ),
            'Adresse':forms.TextInput(attrs={'class':'form-control','placeholder': 'Adresse'} ),
            'image': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            } 

class SalleRegistration(forms.ModelForm):
    class Meta:
        model = Salles
        fields = ['Niveau','Salle','Nbreplace','Professeurprincipal','Planning']
        widgets = {
            'Niveau' : forms.Select(attrs={'class':'form-select'} ),  
            'Nbreplace':forms.TextInput(attrs={'class':'form-control','placeholder': 'Nbreplace'} ),
            'Salle':forms.TextInput(attrs={'class':'form-control','placeholder': 'Institution'} ),
            'Professeurprincipal' : forms.Select(attrs={'class':'form-select'} ), 
            'Planning': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            } 
class SallemRegistration(forms.ModelForm):
    class Meta:
        model = Salles
        fields = ['Niveau','Salle','Nbreplace','Professeurprincipal','Anneescolaire','Etablissement','Planning']
        widgets = {
            'Anneescolaire' : forms.Select(attrs={'class':'form-select'} ), 
            'Etablissement' : forms.Select(attrs={'class':'form-select'} ), 
            'Niveau' : forms.Select(attrs={'class':'form-select'} ),  
            'Nbreplace':forms.TextInput(attrs={'class':'form-control','placeholder': 'Nbreplace'} ),
            'Salle':forms.TextInput(attrs={'class':'form-control','placeholder': 'Institution'} ),
            'Professeurprincipal' : forms.Select(attrs={'class':'form-select'} ), 
            'Planning': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            
            } 

class MoyennemRegistration(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['Note']
        widgets = { 
            'Note':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Nbreplace'} ),
            } 

class EnseignantRegistration(forms.ModelForm):
    class Meta:
        model = Enseignants
        fields = ['Matricule','Nom', 'Prenoms','Datenaissance','Lieunaissance','Telephone','Contact','Email','Ecole','Sexe','Statut', 'Photo']
        widgets = {
            'Matricule':forms.TextInput(attrs={'class':'form-control','placeholder': 'Matricule'} ),
            'Nom':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Prenoms':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Datenaissance':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Lieunaissance':forms.TextInput(attrs={'class':'form-control'} ),
            'Telephone':forms.TextInput(attrs={'class':'form-control','placeholder': 'Telephone'} ),
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact'} ),
            'Email':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact'} ),
            'Photo': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            'Sexe' : forms.Select(attrs={'class':'form-select'} ),
            'Ecole' : forms.Select(attrs={'class':'form-select'} ),
            'Statut' : forms.Select(attrs={'class':'form-select'} ),         
            } 
        
class AnneescolaireRegistration(forms.ModelForm):
    class Meta:
        model = Anneescolaires
        fields = ['Anneescolaire','Statutannee']
        widgets = {
            'Anneescolaire':forms.TextInput(attrs={'class':'form-control','placeholder': 'Anneescolaire'} ),
            'Statutannee' : forms.Select(attrs={'class':'form-select'} ),         
            } 
        
class TypeinstRegistration(forms.ModelForm):
    class Meta:
        model = Typeecoles
        fields = ['Typeecole']
        widgets = {
            'Typeecole':forms.TextInput(attrs={'class':'form-control','placeholder': 'Type d''institution'} ),
            } 

class CatalogueRegistration(forms.ModelForm):
    class Meta:
        model = Catalogues
        fields = ['Nom','Prix']
        widgets = {
            'Nom':forms.TextInput(attrs={'class':'form-control','placeholder': 'Nom'} ),
            'Prix' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Prix'} ),         
            } 

class NiveauRegistration(forms.ModelForm):
    class Meta:
        model = Niveaux
        fields = ['Niveauetude']
        widgets = {
            'Niveauetude':forms.TextInput(attrs={'class':'form-control','placeholder': 'Niveau étude'} ),
            } 
        
class TypematRegistration(forms.ModelForm):
    class Meta:
        model = Typematieres
        fields = ['Typematiere']
        widgets = {
            'Typematiere':forms.TextInput(attrs={'class':'form-control','placeholder': 'Type de matière'} ),
            } 
        
class MatiereRegistration(forms.ModelForm):
    class Meta:
        model = Matieres
        fields = ['Matiere','Professeur','Salle','Typematiere']
        widgets = {
            'Matiere':forms.TextInput(attrs={'class':'form-control','placeholder': 'Matière'} ),
            'Typematiere' : forms.Select(attrs={'class':'form-select'} ), 
            'Salle' : forms.Select(attrs={'class':'form-select'} ), 
            'Professeur' : forms.Select(attrs={'class':'form-select'} ), 
            } 
        
class TimeInput(forms.TextInput):
    input_type = 'time'
class HistoriqueabsRegistration(forms.ModelForm):
    class Meta:
        model = HistoriquesAbs
        fields = ['Cours','Heuredebut','Heurefin']
        widgets = {
            'Cours' : forms.Select(attrs={'class':'form-select'} ),
            'Heuredebut' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}),
            'Heurefin' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}), 
            } 

class SessionRegistration(forms.ModelForm):
    class Meta:
        model = Decoupages
        fields = ['Decoupage','Statutdecoup']
        widgets = {
            'Decoupage':forms.TextInput(attrs={'class':'form-control','placeholder': 'Session'} ),
            'Statutdecoup' : forms.Select(attrs={'class':'form-select'} ), 
            } 
        
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['Title', 'File','Salle','Cours']
        widgets = {
            'Title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Titre'} ),
            'File': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            'Salle' : forms.Select(attrs={'class':'form-select'} ),
            'Salle' : forms.Select(attrs={'class':'form-select'} ),
            'Cours' : forms.Select(attrs={'class':'form-select'} ),
            } 
        
class AutopersRegistration(forms.ModelForm):
    class Meta:
        model = Autorisationspersonnel
        fields = ['Personnel','Service','Poste','Aviss','Contact','Periode','Datedebut','Heuredebut','Datefin','Heurefin','Motif','Datereprise','Heurereprise','Motif','Remplacant','Contactremplacant']
        widgets = {
            'Aviss' : forms.Select(attrs={'class':'form-select'} ),
            'Heuredebut' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}),
            'Heurefin' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}), 
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder': 'Titre'} ),
            'Periode':forms.TextInput(attrs={'class':'form-control','placeholder': 'Titre'} ),
            'Motif':forms.TextInput(attrs={'class':'form-control','placeholder': 'Motif'} ),
            'Remplacant':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            'Contactremplacant':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contactremplacant'} ),
            'Datedebut':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Datefin':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Datereprise':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Heurereprise' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}), 

            'Personnel':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            'Service':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            'Poste':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            } 
        
class AutoensRegistration(forms.ModelForm):
    class Meta:
        model = Autorisationsenseignant
        fields = ['Enseignant','Ecole','Aviss','Contact','Periode','Datedebut','Heuredebut','Datefin','Heurefin','Motif','Datereprise','Heurereprise','Motif','Remplacant','Contactremplacant']
        widgets = {
            'Aviss' : forms.Select(attrs={'class':'form-select'} ),
            'Heuredebut' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}),
            'Heurefin' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}), 
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder': 'Titre'} ),
            'Periode':forms.TextInput(attrs={'class':'form-control','placeholder': 'Titre'} ),
            'Motif':forms.TextInput(attrs={'class':'form-control','placeholder': 'Motif'} ),
            'Remplacant':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            'Contactremplacant':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contactremplacant'} ),
            'Datedebut':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Datefin':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Datereprise':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Heurereprise' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}), 

            'Ecole':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            'Enseignant':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            } 
        
class AutoaudRegistration(forms.ModelForm):
    class Meta:
        model = Autorisationsauditeur
        fields = ['Etudiant','Salle','Aviss','Contact','Periode','Datedebut','Heuredebut','Datefin','Heurefin','Motif','Datereprise','Heurereprise','Motif','Remplacant','Contactremplacant']
        widgets = {
            'Aviss' : forms.Select(attrs={'class':'form-select'} ),
            'Heuredebut' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}),
            'Heurefin' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}), 
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder': 'Titre'} ),
            'Periode':forms.TextInput(attrs={'class':'form-control','placeholder': 'Titre'} ),
            'Motif':forms.TextInput(attrs={'class':'form-control','placeholder': 'Motif'} ),
            'Remplacant':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            'Contactremplacant':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contactremplacant'} ),
            'Datedebut':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Datefin':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Datereprise':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Heurereprise' : forms.TimeInput(attrs={'type': 'time','class':'form-control'}), 
            
            'Etudiant':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            'Salle':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            } 
        

class MisRegistration(forms.ModelForm):
    class Meta:
        model = Missions
        fields = ['Personnel','Service','Poste','Aviss','Lieumission','Datedebut','Datefin','Datemission','Mission','Delegation','Moyen']
        widgets = {
            'Aviss' : forms.Select(attrs={'class':'form-select'} ),
            'Lieumission':forms.TextInput(attrs={'class':'form-control','placeholder': 'Titre'} ),
            'Mission':forms.TextInput(attrs={'class':'form-control','placeholder': 'Mission'} ),

            'Delegation':forms.TextInput(attrs={'class':'form-control','placeholder': 'Delegation'} ),
            'Moyen':forms.TextInput(attrs={'class':'form-control','placeholder': 'Moyen'} ),
            'Datemission':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Datedebut':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Datefin':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),

            'Personnel':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            'Service':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            'Poste':forms.TextInput(attrs={'class':'form-control','placeholder': 'Remplacant'} ),
            } 

class AvisRegistration(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['Aviss']
        widgets = {
            'Aviss':forms.TextInput(attrs={'class':'form-control','placeholder': 'Libelle Avis'} ),
            } 
        
class PersonnelRegistration(forms.ModelForm):
    class Meta:
        model = Personnels
        fields = ['Matricule','Nom', 'Prenoms','Datenaissance','Lieunaissance','Telephone','Contact','Email','Poste','Sexe','Statut', 'Photo','Service']
        widgets = {
            'Matricule':forms.TextInput(attrs={'class':'form-control','placeholder': 'Matricule'} ),
            'Nom':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Prenoms':forms.TextInput(attrs={'class':'form-control','placeholder': 'User name'} ),
            'Datenaissance':forms.DateInput(attrs={'type': 'date','class':'form-control docs-date'} ),
            'Lieunaissance':forms.TextInput(attrs={'class':'form-control'} ),
            'Telephone':forms.TextInput(attrs={'class':'form-control','placeholder': 'Telephone'} ),
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact'} ),
            'Email':forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact'} ),
            'Photo': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            'Sexe' : forms.Select(attrs={'class':'form-select'} ),
            'Service' : forms.Select(attrs={'class':'form-select'} ),
            'Poste' : forms.Select(attrs={'class':'form-select'} ),
            'Statut' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact'} ),  
            } 
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['sujet', 'contenu']
        widgets = {
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }

class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messagess
        fields = ['sujet', 'contenu']
        widgets = {
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }