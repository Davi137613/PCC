from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Usuario(AbstractBaseUser):
    nome= models.CharField(max_length=255)
    data_nascimento= models.DateField()
    data_cadastro= models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128, validators=[MinValueValidator(8)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']
    
    def __str__(self):
        return self.nome

class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(User, related_name='post_curtidas')

    def __str__(self):
        return self.descricao

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(User, related_name='comentario_curtidas')

    def __str__(self):
        return f"Comentário de {self.usuario.username} no post '{self.post.descricao}'"


class Resposta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='respostas')
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resposta de {self.usuario.username} ao comentário de {self.comentario.usuario.username} no post '{self.comentario.post.descricao}'"



class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    artigo = models.ForeignKey('administrador.Artigo', on_delete=models.CASCADE)
    avaliacao = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.artigo.titulo} por {self.usuario.username}"
    
    