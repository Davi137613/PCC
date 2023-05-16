from django.db import models
from django.core.validators import  MinValueValidator


class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    nome= models.CharField(max_length=100)
    data_nascimento= models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128, validators=[MinValueValidator(8)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super(Administrador, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Administrador, self).delete(*args, **kwargs)


class Artigo(models.Model):
    autor = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    subtitulo= models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

