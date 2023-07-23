from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from administrations.models import Ecoles,Etudiants,Enseignants,DossierFinances,DossierScolaires
from administrations.models import Salles, Documents,Anneescolaires,Matieres,Decoupages,Notes,Autorisationsenseignant
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, HttpResponse
from django.core.cache import cache
from django.contrib.auth.hashers import make_password
from django.forms import inlineformset_factory
import uuid
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from administrations.forms import EnseignantRegistration, AnneescolaireRegistration,DocumentForm,MessageForm,MessagesForm
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

@login_required
def etudiantespace(request):
    user = request.user
    etudian = Etudiants.objects.get(User=user.id)
    statuta = Anneescolaires.objects.get(Statutannee='1')
    salle = Salles.objects.filter(Salle=etudian.Salle, Etablissement=etudian.Ecole, Anneescolaire=statuta).get()
    dat = Documents.objects.filter(Salle=salle).order_by('Typematiere')
    etudiados = DossierScolaires.objects.filter(Etudiant=etudian,Anneescolaire=statuta)
    etudiafin = DossierFinances.objects.filter(Etudiant=etudian,Anneescolaire=statuta)
    etudiant = Etudiants.objects.filter(User=user.id)
    sessio = Decoupages.objects.filter(id='2')
    sessi = Decoupages.objects.filter(id='1')
    sessi1 = Decoupages.objects.get(id='1')
    sessio1 = Decoupages.objects.get(id='2')

    sall = Salles.objects.filter(Salle=etudian.Salle, Anneescolaire=statuta)

    grades = Notes.objects.filter(Etudiant=etudian, Anneescolaire=statuta, Decoupage=sessi1)
    grade = Notes.objects.filter(Etudiant=etudian, Anneescolaire=statuta, Decoupage=sessio1)

    form = MessageForm()

    context = {
        'form': form,
        'data': dat,
        'etudiant': etudiant,
        'etudiados': etudiados,
        'etudiafin': etudiafin,
        'sessi': sessi,
        'sessio': sessio,
        'grades': grades,
        'grade': grade,
        'sall': sall,
        'annee': statuta
    }
    return render(request, 'etudiantespace.html', context)



def soumettre_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            etudian = Etudiants.objects.get(User=request.user.id)
            message = form.save(commit=False)
            message.Etudiant = etudian
            message.Nom = etudian.Nom + " " + etudian.Prenoms
            message.Salle = etudian.Salle
            message.save()
            form = MessageForm()  # Réinitialiser le formulaire
            response_data = {'success': True}  # Réponse JSON pour indiquer le succès de la soumission
            return redirect('etudiantespace')
        else:
            response_data = {'success': False, 'errors': form.errors}  # Réponse JSON avec les erreurs de validation du formulaire
            return JsonResponse(response_data)
    else:
        return redirect('etudiantespace')
    
def soumettre_messageens(request):
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            etudian = Enseignants.objects.get(User=request.user.id)
            message = form.save(commit=False)
            message.Enseignant = etudian
            message.Nom = etudian.Nom + " " + etudian.Prenoms
            message.Ecole = etudian.Ecole
            message.save()
            form = MessagesForm()  # Réinitialiser le formulaire
            response_data = {'success': True}  # Réponse JSON pour indiquer le succès de la soumission
            return redirect('enseignantespace')
        else:
            response_data = {'success': False, 'errors': form.errors}  # Réponse JSON avec les erreurs de validation du formulaire
            return JsonResponse(response_data)
    else:
        return redirect('enseignantespace')





@login_required
# Effectif Classe 
def etuclasseauditeur(request, id, iid):
    statuta = Anneescolaires.objects.get(Statutannee='1')
    etud = Etudiants.objects.filter(Salle=id,Ecole=iid).order_by('Nom','Prenoms')
    return render(request,'enseignants/listeauditeur.html', context={'etu':etud,'annee':statuta})

@login_required
# espace etudiant
def enseignantespace(request):
    user=request.user

    enseignant = Enseignants.objects.get(User=user.id)
    matieres = Matieres.objects.filter(Professeur=user.id)
    
    etablissement = Salles.objects.filter()

    
    enseignant = Enseignants.objects.filter(User=user.id)

    statuta = Anneescolaires.objects.get(Statutannee='1')
    sall = Salles.objects.filter(Anneescolaire=statuta)



    annee_scolaire_active = Anneescolaires.objects.get(Statutannee='1')

    # Obtenir le professeur spécifié
    professeur = Enseignants.objects.get(User=user.id)

    # Récupérer toutes les matières associées au professeur spécifié
    matieres_professeur = Matieres.objects.filter(Professeur=professeur)

    # Initialiser une liste vide pour stocker les salles correspondantes
    salles = []

    # Parcourir les matières et récupérer les salles correspondantes
    for matiere in matieres_professeur:
        salle = Salles.objects.filter(Salle=matiere.Salle, Anneescolaire=annee_scolaire_active).first()
        if salle:
            salles.append(salle)

    form = MessagesForm()

    nombre_autorisations = Autorisationsenseignant.objects.filter(Enseignant=professeur).count()
    nombre_salle = Salles.objects.filter(Professeurprincipal=professeur).count()

    return render(request,'enseignantespace.html', context={'form': form,'nombre_autorisations':nombre_autorisations,'nombre_salle':nombre_salle,'docliste':etablissement,'enseignant':enseignant,'sall':sall,'annee':statuta,'salles': salles})

@login_required
# espace etudiant
def espaceliste(request,id,iid):
    # Récupérer l'objet à partir de l'ID fourni
    salle = Salles.objects.get(id=id)
    statuta = Anneescolaires.objects.get(Statutannee='1')
    data = Documents.objects.filter(Salle=salle,Anneescolaire=statuta).order_by('Typematiere')


    enseignant = Enseignants.objects.get(User=iid)
    salle = Salles.objects.get(id=id)
    matiere = Matieres.objects.filter(Professeur=enseignant, Salle=salle).first()
    
    if matiere:
        documents = Documents.objects.filter(Cours=matiere,Anneescolaire=statuta)
    else:
        documents = []

    context = {
        'documents': documents,
        'data':data,'annee':statuta
    }

    
    return render(request,'enseignants/listedoc.html', context)

# Ajouter
def add_documentp(request, object_id):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            statuta = Anneescolaires.objects.get(Statutannee='1')
            course_id = request.POST['course']
            form.save()
            return redirect('document_list')
    else:
        courses = Matieres.objects.filter(Salle=object_id).order_by('Typematiere')
        statuta = Anneescolaires.objects.get(Statutannee='1')
        context = {
            'courses': courses,'annee':statuta
        }
        form = DocumentForm(context)
    return render(request, 'enseignants/adddoc.html', {'form': form} )

