# authentication/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Utilisateur

class UtilisateurForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Utilisateur
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'role', 'statut', 'profile_photo']
        widgets = {
            'role' : forms.Select(attrs={'class':'form-select'} ),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Login'} ),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Nom'} ),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Prénoms'} ),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control','type':'file'}),
            'password': forms.TextInput(attrs={'class':'form-control','placeholder': 'Mot de passe'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'} ),
            } 

class UtilisateurUpdateForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'statut', 'profile_photo']


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'password')