from django import forms
from .models import Psicologo

class PsicologoForm(forms.ModelForm):
    class Meta:
        model = Psicologo
        fields = ['nome', 'senha', 'email', 'crp', 'data_nascimento']
