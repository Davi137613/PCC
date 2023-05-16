from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Moderador
from .forms import ModeradorForm

@login_required
def moderador_list(request):
    moderadores = Moderador.objects.all()
    return render(request, 'moderador_list.html', {'moderadores': moderadores})



@login_required
def moderador_create(request):
    if request.method == 'POST':
        form = ModeradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Moderador criado com sucesso.')
            return redirect('moderador_list')
    else:
        form = ModeradorForm()
    return render(request, 'moderador_form.html', {'form': form})



@login_required
def moderador_update(request, pk):
    moderador = get_object_or_404(Moderador, pk=pk)
    if request.method == 'POST':
        form = ModeradorForm(request.POST, instance=moderador.user)
        if form.is_valid():
            form.save()
            moderador.data_nascimento = form.cleaned_data['data_nascimento']
            moderador.save()
            messages.success(request, 'Moderador atualizado com sucesso.')
            return redirect('moderador_list')
    else:
        form = ModeradorForm(instance=moderador.user, initial={'data_nascimento': moderador.data_nascimento})
    return render(request, 'moderador_form.html', {'form': form})



@login_required
def moderador_delete(request, pk):
    moderador = get_object_or_404(Moderador, pk=pk)
    user = moderador.user
    moderador.delete()
    user.delete()
    messages.success(request, 'Moderador excluído com sucesso.')
    return redirect('moderador_list')
