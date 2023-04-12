from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Psicologo(models.Model):
    crp= models.CharField(max_length=255)
    nome= models.CharField(max_length=100)
    data_nascimento= models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128, validators=[MinValueValidator(8)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']
    

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    psicologo = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(default=timezone.now)
    motivo = models.TextField()


    def __str__(self):
        return f"Agenda de {self.psicologo.username}"
    