from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Usuario(AbstractBaseUser):
    nome= models.CharField(max_length=255)
    data_nascimento= models.DateField(blank=True, null=True)
    data_cadastro= models.DateField(auto_now_add=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128, validators=[MinValueValidator(8)])


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']
    
    def __str__(self):
        return self.nome


class Post(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(Usuario, related_name='post_curtidas')

    def __str__(self):
        return f"Post de {self.usuario.nome}"


class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentario')
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(Usuario, blank=True, related_name='comentario_curtidas')

    def __str__(self):
        return f"Comentário de {self.usuario.nome} no post {self.post.id}"


class Resposta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='resposta')
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    curtidas = models.ManyToManyField(Usuario, blank=True, related_name= 'curtidas_resposta')

    def __str__(self):
        return f"Resposta de {self.usuario.nome} ao comentário de {self.comentario.usuario.nome} no post {self.comentario.post.id}"


class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    artigo = models.ForeignKey('administrador.Artigo', on_delete=models.CASCADE)
    avaliacao = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.artigo.titulo} por {self.usuario.nome}"
    
    