from django.db import models
from django.contrib.auth import get_user_model



Usuario = get_user_model()


class Perfil(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_usuario = models.IntegerField()
    bio = models.TextField(blank=True)
    perfilimg = models.ImageField(upload_to='perfil_images', default='foto_perfil_branca.png')
    localizacao = models.CharField(max_length=100, blank=True)

