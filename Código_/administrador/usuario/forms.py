from django import forms
from.models import usuario

class usuarioForm(forms.ModelForm):
    class Meta: 
        model= usuario
        fields = ['nome', 'email', 'data_nascimento', 'senha']
