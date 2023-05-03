from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AdministradorForm, AdministradorUpdateForm
from .models import Administrador


@login_required
def administrador_create(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            Administrador.objects.create(user=user, email=form.cleaned_data['email'], data_nascimento=form.cleaned_data['data_nascimento'])
            return redirect('administrador_list')
    else:
        form = AdministradorForm()
    return render(request, 'administrador_create.html', {'form': form})


@login_required
def administrador_list(request):
    administradores = Administrador.objects.all()
    return render(request, 'administrador_list.html', {'administradores': administradores})


@login_required
def administrador_update(request, pk):
    administrador = get_object_or_404(Administrador, pk=pk)
    if request.method == 'POST':
        form = AdministradorUpdateForm(request.POST, instance=administrador.user)
        if form.is_valid():
            form.save()
            administrador.email = form.cleaned_data['email']
            administrador.data_nascimento = form.cleaned_data['data_nascimento']


@login_required
def administrador_delete(request, pk):
    admin = get_object_or_404(Administrador, pk=pk)
    if request.method == 'POST':
        admin.delete()
        return redirect('admin_list')
    return render(request, 'admin_delete.html', {'admin': admin})
            

