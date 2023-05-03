from django.db import models
from django.core.validators import MinValueValidator


class Moderador(models.Model):
    nome= models.CharField(max_length=100)
    data_nascimento= models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128, validators=[MinValueValidator(8)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome