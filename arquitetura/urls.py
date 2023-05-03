from django.urls import path
from arquitetura import views

urlpatterns = [
   path('', views.pagprincipal, name='pag-principal'),
   path('', views.base, name='base'),
]



