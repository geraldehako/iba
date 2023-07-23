# authentication/views.py
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UtilisateurForm, UtilisateurUpdateForm
from .models import Utilisateur
from django.utils import timezone
from administrations.models import License
from django.contrib.auth.hashers import make_password

def inscription_utilisateur(request):
    if request.method == 'POST':
        fm = UtilisateurForm(request.POST, request.FILES)
        if fm.is_valid():
            photo = fm.cleaned_data['profile_photo']
            userna = fm.cleaned_data['first_name']
            usernam = fm.cleaned_data['last_name']
            FString = userna + " " + usernam
            username = fm.cleaned_data['username']
            role = fm.cleaned_data['role']
            password = fm.cleaned_data['password']
            statu = 'ACTIVE'
            stat = '0'
            sta = '0'
            profile_photo = photo
            encoded_password = make_password(password)
            email = fm.cleaned_data['email']
            userm = Utilisateur.objects.create(
                is_active=sta,
                is_staff=stat,
                statut=statu,
                profile_photo=photo,
                username=username,
                last_name=usernam,
                first_name=userna,
                password=encoded_password,
                email=email,
                role=role
            )
            
            # Autres traitements après l'inscription
            return redirect('user')
    else:
        fm = UtilisateurForm()

    context = {
        'form': fm
    }


    return render(request, 'Pages/users/add.html', context)

def modifier_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)

    if request.method == 'POST':
        form = UtilisateurUpdateForm(request.POST, request.FILES, instance=utilisateur)
        if form.is_valid():
            form.save()
            # Autres traitements après la modification de l'utilisateur
            return redirect('user')
    else:
        form = UtilisateurUpdateForm(instance=utilisateur)

    context = {
        'form': form
    }
    return render(request, 'Pages/users/modif.html', context)

def supprimer_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)

    if request.method == 'POST':
        utilisateur.delete()
        # Autres traitements après la suppression de l'utilisateur
        return redirect('user')

    context = {
        'utilisateur': utilisateur
    }
    return render(request, 'supprimer_utilisateur.html', context)


# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if request.user.role == 'GESTIONNAIRE':
                return redirect('dashboardcaisse')
            elif request.user.role == 'ENSEIGNANT':
                return redirect('enseignantespace')
            elif request.user.role == 'ETUDIANT':
                return redirect('etudiantespace')
            elif request.user.role == 'ADMINISTRATEUR':
                return redirect('menu')
            elif request.user.role == 'DIRECTION':
                return redirect('dashboardrh')
            elif request.user.role == 'ACADEMIQUE':
                return redirect('dashboardacademique')
            elif request.user.role == 'ADMINISTRATEURSUPER':
                return redirect('dashboard')
            
        
    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')



def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
           # login_user(request, user)
          #  return redirect(settings.LOGIN_REDIRECT_URL)
        
    return render(request, 'accounts/signup.html', context={'form': form})



