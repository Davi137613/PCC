from django.shortcuts import render, redirect
from.models import Usuario
from.forms import UsuarioForm
from .models import Usuario


def list_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario.html', {'usuario': usuarios})


def create_usuarios(request):
    form= UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_usuarios')
    
    return render(request, 'usuarioForm.html', {'form': form})


def update_usuarios(request, id):
    usuarios = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST or None, instance=usuarios)

    if form.is_valid():
        form.save()
        return redirect('list_usuarios')
    
    return render(request, 'usuarioForm.html', {'form': form, 'usuario': usuarios})


def delete_usuarios(request, id):
    usuarios= Usuario.objects.get(id=id)

    if request.method =='POST':
        usuarios.delete()
        return redirect('list_usuarios')
    
    return render(request, 'usuario_delete_confirm.html', {'usuario': usuarios})











