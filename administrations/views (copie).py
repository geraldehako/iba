from django.shortcuts import render
from administrations.models import Notes
from administrations.models import Etudiants, Matieres, Anneescolaires,Statutannees, Moyennes, Decoupages,Documents
from administrations.models import Ecoles
from administrations.models import Salles
from accounts.models import Utilisateur
from .forms import EtudiantRegistration
from .forms import EcoleRegistration
from .forms import EnseignantRegistration, AnneescolaireRegistration,DocumentForm,SalleRegistration,SallemRegistration
from accounts.forms import UserCreationForm
from .models import Enseignants
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, HttpResponse
from django.core.cache import cache
from django.contrib.auth.hashers import make_password
from django.forms import inlineformset_factory
import uuid
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
# DASHBOARD...................................................................................................................................
@login_required(login_url='/accounts/')
def dashboard(request):

    statuta = Anneescolaires.objects.get(Statutannee='1')
    salle = Salles.objects.filter(Anneescolaire=statuta)
    for sal in salle:
        num_students = Etudiants.objects.filter(Salle=sal).count()
        context = {
            'num_students': num_students,
         }
    num_salle = Salles.objects.filter( Anneescolaire=statuta).count()
    context = {
            'num_salle': num_salle,
         }  
    return render(request,'Pages/dashboard.html', context)



# liste etudiant
@login_required(login_url='/accounts/')
def etu(request):
    etud = Etudiants.objects.all()
    return render(request,'Pages/etudiants/liste.html', context={'etu':etud})

# liste par classe etudiant
@login_required(login_url='/accounts/')
def etuclasse(request, id, iid):
    etud = Etudiants.objects.filter(Salle=id,Ecole=iid).order_by('Nom','Prenoms')
    return render(request,'Pages/etudiants/listeclasse.html', context={'etu':etud})

# liste par classe etudiant template
@login_required(login_url='/accounts/')
def etuclassetemplate(request, id, iid):
    etud = Etudiants.objects.filter(Salle=id,Ecole=iid).order_by('Nom','Prenoms')
    return render(request,'Pages/etudiants/listeclassetemplate.html', context={'etu':etud})

# ajouter etudiant
def add_etudiant(request):
    if request.method == 'POST':
        fm = EtudiantRegistration(request.POST, request.FILES)
        if fm.is_valid():
            messages.success(request, 'Votre formulaire a été envoyé avec succès !')
            photo = fm.cleaned_data['Photo']
            fm.save()
            return redirect('liste')
    else :
        fm = EtudiantRegistration()
    return render(request,'Pages/etudiants/add.html',{'form':fm}  )

# ajouter etudiant
def addd_etudiant(request):
    if request.method == 'POST':
        fm = EtudiantRegistration(request.POST, request.FILES)
        if fm.is_valid():
            messages.success(request, 'Votre formulaire a été envoyé avec succès !')
            photo = fm.cleaned_data['Photo']
            student = fm.save(commit=False)
            student.save()
            # Créer un utilisateur avec le même nom d'utilisateur et mot de passe que l'étudiant
            userna = fm.cleaned_data['Nom']
            usernam = fm.cleaned_data['Prenoms']
            FString = userna + " " + usernam
            username = FString
            role = 'ETUDIANT'
            password = 'P@ssword'
            profile_photo=photo
            encoded_password = make_password(password)
            email = fm.cleaned_data['Email']
            userm = Utilisateur.objects.create(profile_photo=profile_photo,username=username,last_name=usernam,first_name=userna, password=encoded_password, email=email,role=role)

            # Ajouter l'utilisateur à l'objet Etudiant et enregistrer à nouveau
            student.User = userm
            student.save()
            return redirect('liste')
    else :
        matricule = str(uuid.uuid4())[:8] # génération d'une chaîne aléatoire de 8 caractères
        fm = EtudiantRegistration(initial={'Matricule': matricule})
    return render(request,'Pages/etudiants/add.html',{'form':fm}  )




# ECOLE
# liste 
def ecoleliste(request):
    etablissement = Ecoles.objects.all()
    return render(request,'Pages/ecoles/liste.html', context={'ecoleliste':etablissement})
# ajouter
def ecoleajout(request):
    if request.method == 'POST':
        fm = EcoleRegistration(request.POST, request.FILES)
        if fm.is_valid():
            image = fm.cleaned_data['image']
            fm.save()
            messages.success(request, 'Votre formulaire a été envoyé avec succès !')
            fm = EcoleRegistration()
            return redirect('ecoleliste')
    else :
        fm = EcoleRegistration()
    return render(request,'Pages/ecoles/ajout.html',{'form':fm}  )
# modifier
def ecolemodif(request, id):
    if request.method == 'POST':
        pi = Ecoles.objects.get(pk=id)
        fm = EcoleRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('ecoleliste')
    else:
        pi = Ecoles.objects.get(pk=id)
        fm = EcoleRegistration(instance=pi)
    return render(request, 'Pages/ecoles/modif.html',{'form':fm})

# supprimer
def delete_object(request, id):
    pi = Ecoles.objects.get(pk=id)
    if request.method == 'POST':
        pi.delete()
        return redirect('ecoleliste')  # rediriger vers la liste des objets

    # Afficher le formulaire de confirmation de suppression
    context = {'object': pi}
    return render(request, 'myapp/delete_object.html', context)


# SALLE DE CLASSE------------------------------------------------------------------------------------------------------------
# ajouter classe
def add_classe(request,id):
    statuta = Anneescolaires.objects.get(Statutannee='1')
    salle = Ecoles.objects.get(id=id)
    if request.method == 'POST':
        fm = SalleRegistration(request.POST)
        if fm.is_valid():
            messages.success(request, 'Votre formulaire a été envoyé avec succès !')
            Sal = fm.cleaned_data['Salle']
            Nbre = fm.cleaned_data['Nbreplace']
            Prof = fm.cleaned_data['Professeurprincipal']
            Niv = fm.cleaned_data['Niveau']
            grade = Salles.objects.create( Nbreplace=Nbre,Niveau=Niv, Anneescolaire=statuta, Salle=Sal, Etablissement=salle, Professeurprincipal=Prof)
            return redirect('ecoleliste')
    else :
        fm = SalleRegistration()
    return render(request,'Pages/salles/add.html',{'form':fm}  )

# modifier
def classmodif(request, id):
    if request.method == 'POST':
        pi = Salles.objects.get(pk=id)
        fm = SallemRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('ecoleliste')
    else:
        pi = Salles.objects.get(pk=id)
        fm = SallemRegistration(instance=pi)
    return render(request, 'Pages/salles/modif.html',{'form':fm})

# Effectif Classe 
def listesalle(request, object_id):
    # Récupérer l'objet à partir de l'ID fourni
    salle = Salles.objects.get(id=object_id)
    
    # Récupérer les données triées en fonction de l'objet
    data = Salles.objects.filter(object=salle).order_by('Niveau')

    # Passer les données triées en contexte au template
    context = {'object': salle, 'data': data}
    return render(request, 'Pages/salles/salleecole.html', context)

def object_table(request, id):
   
    statuta = Anneescolaires.objects.get(Statutannee='1')
    # Récupérer les données triées en fonction de l'objet
    queryset = Salles.objects.filter(Etablissement=id, Anneescolaire=statuta).order_by('Niveau')

    # Passer les données triées en contexte au template
    context = {'queryset': queryset}
    return render(request, 'Pages/salles/salleecole.html', context)



# DOCUMENT DE CLASSE------------------------------------------------------------------------------------------------------------
# Liste Document 
def listedoc(request):
   
    statuta = Anneescolaires.objects.get(Statutannee='1')
    # Récupérer les données triées en fonction de l'objet
    queryse = Documents.objects.all()

    # Passer les données triées en contexte au template
    context = {'queryse': queryse}
    return render(request, 'Pages/documents/listedoc.html', context)

# Ajouter Document
def add_document(request):
    statuta = Anneescolaires.objects.get(Statutannee='1')
    
    if request.method == 'POST':
        
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            Fil = form.cleaned_data['Cours']
            Typ = Matieres.objects.get(Matiere=Fil)
            File = form.cleaned_data['File']
            Title = form.cleaned_data['Title']
            ids = form.cleaned_data['Salle']
            student = form.save(commit=False)
            userm = Documents.objects.create(Anneescolaire=statuta,Cours=Fil,File=File,Title=Title,Salle=ids,Typematiere=Typ.Typematiere)
            userm.save()
            
            return redirect('documentlist')
    else:
        
        form = DocumentForm()
    return render(request, 'Pages/documents/ajoutdoc.html', {'form': form})


# Detail
def document_detail(request, document_id):
    document = Documents.objects.get(id=document_id)
    return FileResponse(document.File)

# Telecharger
def document_download(request, document_id):
    document = Documents.objects.get(id=document_id)
    response = HttpResponse(document.File, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{document.File.name}"'
    return response


# ANNEES SCOLAIRES------------------------------------------------------------------------------------------------------------
# liste 
def anneescolaireliste(request):
    anneescolaire = Anneescolaires.objects.all()
    return render(request,'Pages/anneescolaires/liste.html', context={'anneescolaireliste':anneescolaire})
# ajouter
def anneescolaireajout(request):
    if request.method == 'POST':
        fm = AnneescolaireRegistration(request.POST)
        if fm.is_valid():
            
            fm.save()
            messages.success(request, 'Votre formulaire a été envoyé avec succès !')
            fm = AnneescolaireRegistration()
            return redirect('anneescolaireliste')
    else :
        fm = AnneescolaireRegistration()
    return render(request,'Pages/anneescolaires/ajout.html',{'form':fm}  )

# Modifier statut
def anneescolairestatut(request, id):
    statuta = Statutannees.objects.get(Statutannee='ACTIF')
    statuti = Statutannees.objects.get(Statutannee='INACTIF')
    anneestatut = Anneescolaires.objects.get(id=id)
    if anneestatut.Statutannee==statuta :
        anneestatut.Statutannee=statuti
        anneestatut.save()
    else :
        anneestatut.Statutannee=statuta
        anneestatut.save()

# ENSEIGNANTS------------------------------------------------------------------------------------------------------------
# liste 
def enseignantliste(request):
    enseignant = Enseignants.objects.all()
    return render(request,'Pages/enseignants/liste.html', context={'enseignantliste':enseignant})
# ajouter
def enseignantajout(request):
    if request.method == 'POST':
        fm = EnseignantRegistration(request.POST, request.FILES)
        if fm.is_valid():
            Photo = fm.cleaned_data['Photo']
            student = fm.save(commit=False)
            student.save()
            # Créer un utilisateur avec le même nom d'utilisateur et mot de passe que l'étudiant
            userna = fm.cleaned_data['Nom']
            usernam = fm.cleaned_data['Prenoms']
            FString = userna + " " + usernam
            username = FString
            role = 'ENSEIGNANT'
            password = 'P@ssword'
            profile_photo = Photo
            encoded_password = make_password(password)
            email = fm.cleaned_data['Email']
            userm = Utilisateur.objects.create(profile_photo=profile_photo,username=username,last_name=usernam,first_name=userna, password=encoded_password, email=email,role=role)

            # Ajouter l'utilisateur à l'objet Etudiant et enregistrer à nouveau
            student.User = userm
            student.save()
            return redirect('enseignantliste')
    else :
        matricule = str(uuid.uuid4())[:8] # génération d'une chaîne aléatoire de 8 caractères
        fm = EnseignantRegistration(initial={'Matricule': matricule})
    return render(request,'Pages/enseignants/ajout.html',{'form':fm}  )

# NOTES------------------------------------------------------------------------------------------------------------

def add_grade(request,object_id,objec_id):
    if request.method == 'POST':
        statuta = Anneescolaires.objects.get(Statutannee='1')
        statuti = Decoupages.objects.get(Statutdecoup='1')
        course_id = request.POST['course']
        score = request.POST.get('score', None)
        if score is not None:
            score = float(score)
            if 19.0 <= score <= 20.0:
                
                
                app = "Excellent"
                student = Etudiants.objects.get(id=object_id)
                course = Matieres.objects.get(id=course_id)
                grade = Notes.objects.create( Etudiant=student,Appreciation=app, Cours=course, Note=score, Anneescolaire=statuta, Decoupage=statuti, Salle=student.Salle,  Professeur=course.Professeur, Typematiere=course.Typematiere)
                messages.success(request, f"Grade added for {course.Matiere}")
                return redirect('liste')
            elif 17.0 <= score <= 18.75:
                app = "Très Bien"
                
                student = Etudiants.objects.get(id=object_id)
                course = Matieres.objects.get(id=course_id)
                grade = Notes.objects.create( Etudiant=student,Appreciation=app, Cours=course, Note=score, Anneescolaire=statuta, Decoupage=statuti, Salle=student.Salle,  Professeur=course.Professeur, Typematiere=course.Typematiere)
                messages.success(request, f"Grade added for {course.Matiere}")
                return redirect('liste')
            elif 15.0 <= score <= 16.99:
                app = "Bien"
                
                student = Etudiants.objects.get(id=object_id)
                course = Matieres.objects.get(id=course_id)
                grade = Notes.objects.create( Etudiant=student,Appreciation=app, Cours=course, Note=score, Anneescolaire=statuta, Decoupage=statuti, Salle=student.Salle,  Professeur=course.Professeur, Typematiere=course.Typematiere)
                messages.success(request, f"Grade added for {course.Matiere}")
                return redirect('liste')
            elif 13.0 <= score <= 14.99:
                app = "Assez Bien"
                
                student = Etudiants.objects.get(id=object_id)
                course = Matieres.objects.get(id=course_id)
                grade = Notes.objects.create( Etudiant=student,Appreciation=app, Cours=course, Note=score, Anneescolaire=statuta, Decoupage=statuti, Salle=student.Salle,  Professeur=course.Professeur, Typematiere=course.Typematiere)
                messages.success(request, f"Grade added for {course.Matiere}")
                return redirect('liste')
            elif 11.0 <= score <= 12.99:
                app = "Passable"
                
                student = Etudiants.objects.get(id=object_id)
                course = Matieres.objects.get(id=course_id)
                grade = Notes.objects.create( Etudiant=student,Appreciation=app, Cours=course, Note=score, Anneescolaire=statuta, Decoupage=statuti, Salle=student.Salle,  Professeur=course.Professeur, Typematiere=course.Typematiere)
                messages.success(request, f"Grade added for {course.Matiere}")
                return redirect('liste')
            elif 0 <= score <= 10.99:
                app = "Faible"
               
                student = Etudiants.objects.get(id=object_id)
                course = Matieres.objects.get(id=course_id)
                grade = Notes.objects.create( Etudiant=student,Appreciation=app, Cours=course, Note=score, Anneescolaire=statuta, Decoupage=statuti, Salle=student.Salle,  Professeur=course.Professeur, Typematiere=course.Typematiere)
                messages.success(request, f"Grade added for {course.Matiere}")
                return redirect('liste')
            else:
                app = "Score out of range"
        else:
            app = "No score provided"
        return app

        
    else:
        courses = Matieres.objects.filter(Salle=objec_id).order_by('Typematiere')
        context = {
            'courses': courses,
        }
        return render(request, 'Pages/bulletins/ajoutnote.html', context)
    
def home(request,id):
    student = Etudiants.objects.get(id=id)
    grades = Notes.objects.filter(Etudiant=student)
    context = {
        'student': student,
        'grades': grades,
    }
    return render(request, 'Pages/bulletins/listenote.html', context)

# MOYENNES------------------------------------------------------------------------------------------------------------
# Calcul moyennes
def calculate_results(request,id,iid):
    
    statuta = Anneescolaires.objects.get(Statutannee='1')
    statuti = Decoupages.objects.get(Statutdecoup='1')
    students = Etudiants.objects.prefetch_related('Salle').filter(Salle=id,Ecole=iid)
    for student in students:
        results = Notes.objects.filter(Etudiant=student,  Anneescolaire=statuta, Decoupage=statuti)
        total_score = 0
        for result in results:
            total_score += result.Note # type: ignore
        if len(results) > 0:
            avg_score = total_score / len(results) # calcule la moyenne
        else:
            avg_score = 0 # si aucun résultat, la moyenne est zéro
        # Update student's average score in the database
        grade = Moyennes.objects.create( Etudiant=student, Moyenne=avg_score ,Total=total_score, Anneescolaire=statuta, Decoupage=statuti)
        

    # Get all students sorted by their average score
    ranked_students = Moyennes.objects.all().order_by('-Moyenne')
    # Assign a rank to each student based on their average score
    rank = 1
    for student in ranked_students:
        student.Rang = rank # type: ignore
        student.save()
        rank += 1

    return redirect('ecoleliste')

# Afficher les bulletins de la classe
def homebu(request,id):
    statuta = Anneescolaires.objects.get(Statutannee='1')
    statuti = Decoupages.objects.get(Statutdecoup='1')

    
    books = Moyennes.objects.select_related('Etudiant').all()
    for book in books:
        print("Moyenne :", book.Moyenne)
        print("Etudiant :", book.Etudiant.Nom, book.Etudiant.Prenoms)
    
    data = []
    for book in books:
        
        etudiantn = book.Etudiant.Nom
        etudiantp = book.Etudiant.Prenoms
        etudiants = book.Etudiant.Salle
        moyenne = book.Moyenne
        moyenned = book.Decoupage
        moyennea = book.Anneescolaire
        moyennet = book.Total
        moyenner = book.Rang
      
        data.append({'etudiantn': etudiantn,
                     'etudiantp': etudiantp,
                     'etudiants': etudiants,
                     'moyenned': moyenned,
                     'moyennea': moyennea,'moyennet': moyennet,'moyenner': moyenner,
                       'moyenne': moyenne})
        
    students = Etudiants.objects.prefetch_related('Salle').filter(Salle=id)
    for student in students:
        boo = Notes.objects.select_related('Etudiant').distinct().filter(Anneescolaire=statuta,Decoupage=statuti,Salle=id,Etudiant=student)
        dat = []
        for bo in boo:
            notem = bo.Cours
            notev = bo.Note
            notep = bo.Professeur
            notea = bo.Appreciation
            notet = bo.Typematiere

            dat.append({'notem': notem,
                        'notep': notep,
                        'notea': notea,
                        'notet': notet,
                     'notev': notev})

        return render(request, 'Pages/bulletins/resultat.html', context={'data': data,'dat': dat})
    


# DOCUMENTS ESPACE ENSEIGNANT------------------------------------------------------------------------------------------------------------
# Ajouter
def add_documente(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'add_document.html', {'form': form})


# Detail
def document_detaile(request, document_id):
    document = Documents.objects.get(id=document_id)
    return FileResponse(document.File)

# Ajouter
def document_downloade(request, document_id):
    document = Documents.objects.get(id=document_id)
    response = HttpResponse(document.File, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{document.File.name}"'
    return response

# DOCUMENTS ESPACE ENSEIGNANT------------------------------------------------------------------------------------------------------------
# Ajouter