from django.db import models

class Administrador(models.Model):
    nome= models.CharField(max_length=255)
    senha= models.CharField(max_length=255)
    data_nascimento= models.DateField()
    email= models.EmailField()

class Artigo(models.Model):
    titulo= models.CharField(max_length=255)
    subtitulo= models.CharField(max_length=255, blank=True, null=True)
    conteudo= models.CharField(max_length=255)
    data_publi= models.DateField()


class Moderador(models.Model):
    nome= models.CharField(max_length=255)
    senha= models.CharField(max_length=255)
    data_nascimento= models.DateField()
    email= models.EmailField()

class Usuario(models.Model):
    nome= models.CharField(max_length=255)
    senha= models.CharField(max_length=255)
    data_nascimento= models.DateField()
    data_cadastro= models.DateField()
    email= models.EmailField()

class Post(models.Model):
    conteudo= models.CharField(max_length=255)
    data_publi= models.DateField()

class Psicologo(models.Model):
    nome= models.CharField(max_length=255)
    senha= models.CharField(max_length=255)
    data_nascimento= models.DateField()
    email= models.EmailField()
    cfp= models.CharField(max_length=255)
