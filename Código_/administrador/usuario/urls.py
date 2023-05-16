from django.urls import path
from .views import create_usuarios, list_usuarios

urlpatterns = [
    path('', list_usuarios, name= 'list_usuarios'),
    path('new', create_usuarios, name='create_usuarios'),
    path('update/<int:id>/', update_usuarios, name='update_usuarios'),
    path('delete/<int:id>/', delete_usuarios, name='delete_usuarios'),
]