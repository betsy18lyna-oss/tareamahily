from django.shortcuts import render, redirect
from .forms import EquipoForm

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = EquipoForm()
    return render(request, 'equipos/crear_equipo.html', {'form': form})