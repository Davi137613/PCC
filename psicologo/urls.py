
from django.urls import path
from . import views

urlpatterns = [
    path('', views.psicologo_list, name='psicologo_list'),
    path('', views.psicologo_detail, name='psicologo_detail'),
    path('', views.psicologo_new, name='psicologo_new'),
    path('', views.psicologo_edit, name='psicologo_edit'),
    path('', views.psicologo_delete, name='psicologo_delete'),
]
    
