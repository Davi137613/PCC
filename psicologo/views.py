from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Psicologo
from .forms import PsicologoForm


@login_required
def psicologo_list(request):
    psicologos = Psicologo.objects.all()
    return render(request, 'app_psicologo/psicologo_list.html', {'psicologos': psicologos})


@login_required
def psicologo_detail(request, pk):
    psicologo = get_object_or_404(Psicologo, pk=pk)
    return render(request, 'app_psicologo/psicologo_detail.html', {'psicologo': psicologo})


@login_required
def psicologo_new(request):
    if request.method == "POST":
        form = PsicologoForm(request.POST)
        if form.is_valid():
            psicologo = form.save(commit=False)
            psicologo.save()
            return redirect('psicologo_detail', pk=psicologo.pk)
    else:
        form = PsicologoForm()
    return render(request, 'app_psicologo/psicologo_edit.html', {'form': form})


@login_required
def psicologo_edit(request, pk):
    psicologo = get_object_or_404(Psicologo, pk=pk)
    if request.method == "POST":
        form = PsicologoForm(request.POST, instance=psicologo)
        if form.is_valid():
            psicologo = form.save(commit=False)
            psicologo.save()
            return redirect('psicologo_detail', pk=psicologo.pk)
    else:
        form = PsicologoForm(instance=psicologo)
    return render(request, 'app_psicologo/psicologo_edit.html', {'form': form})


@login_required
def psicologo_delete(request, pk):
    psicologo = get_object_or_404(Psicologo, pk=pk)
    psicologo.delete()
    return redirect('psicologo_list')
