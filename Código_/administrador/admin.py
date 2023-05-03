from django.contrib import admin
from administrador.models import Administrador, Artigo


admin.site.register(Administrador)
admin.site.register(Artigo)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
