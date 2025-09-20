from django.shortcuts import render, redirect
from .forms import EquipoForm, CustomUserCreationForm
from .models import Equipo

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'users/crear_equipo.html', {'form': form})

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'users/lista_equipos.html', {'equipos': equipos})

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/registro.html', {'form': form})
