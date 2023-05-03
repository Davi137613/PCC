from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Moderador

class ModeradorForm(UserCreationForm):
    email = forms.EmailField()
    data_nascimento = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'data_nascimento']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            moderador = Moderador.objects.create(user=user, data_nascimento=self.cleaned_data['data_nascimento'])
            moderador.save()
        return user
