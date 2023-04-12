from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Administrador(models.Model):
    nome= models.CharField(max_length=100)
    data_nascimento= models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128, validators=[MinValueValidator(8)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']


    def __str__(self):
        return self.nome


class Artigo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    subtitulo= models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

