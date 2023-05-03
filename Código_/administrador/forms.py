from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AdministradorForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Digite um e-mail válido.')
    data_nascimento = forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class AdministradorUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Digite um e-mail válido.')
    data_nascimento = forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'email', )

class AdministradorDeleteForm(forms.ModelForm):

    class Meta:
        model = User
        fields = []
