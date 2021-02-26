from django import forms 
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30,
                               help_text="Le nom d'utilisateur ne doit pas contenir d'espaces")
    email = forms.EmailField(label='Adresse électronique')
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom de famille')
    password1 = forms.CharField(
        label='Mot de passe ', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label='Confirmez le mot de passe', widget=forms.PasswordInput(), min_length=8)
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","password1","password2")
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Le mot de passe ne correspond pas')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('Ce compte est déjà existé')
        return cd['username']