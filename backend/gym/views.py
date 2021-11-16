from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib import messages


def ClaseView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(Clase, id=pk)
        if request.method == 'POST':
            form = ClaseForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = ClaseForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/clase/')
                else:
                    messages.error(request, form.errors)
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    form.save()
                    return redirect(f'/clase/{pk}/')
                messages.error(request, form.errors)
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                if Clase.objects.filter(pk=pk).count() > 0:
                    return redirect(f'/clase/{pk}/')
                else:
                    messages.error(request, "Clase no encontrada")
                    form = ClaseForm()
        else:
            form = ClaseForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            form = ClaseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/clase/')
            else:
                messages.error(request, form.errors)
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None or Clase.objects.filter(pk=pk).count() <= 0:
                messages.error(request, "Clase no encontrada")
                form = ClaseForm()
            else:
                return redirect(f'/clase/{pk}/')
    else:
        form = ClaseForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'util/form.html', context)


def CalendarioView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(Calendario, id=pk)
        if request.method == 'POST':
            form = CalendarioForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = CalendarioForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/calendario/')
                else:
                    messages.error(request, form.errors)
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    form.save()
                    return redirect(f'/calendario/{pk}/')
                messages.error(request, form.errors)
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                if Calendario.objects.filter(pk=pk).count() > 0:
                    return redirect(f'/calendario/{pk}/')
                else:
                    messages.error(request, "Calendario no encontrada")
                    form = CalendarioForm()
        else:
            form = CalendarioForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            form = CalendarioForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/calendario/')
            else:
                messages.error(request, form.errors)
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None or Calendario.objects.filter(pk=pk).count() <= 0:
                messages.error(request, "Calendario no encontrada")
                form = CalendarioForm()
            else:
                return redirect(f'/calendario/{pk}/')
    else:
        form = CalendarioForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'util/form.html', context)


def ZonaView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(Zona, id=pk)
        if request.method == 'POST':
            form = ZonaForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = ZonaForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/zona/')
                else:
                    messages.error(request, form.errors)
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    form.save()
                    return redirect(f'/zona/{pk}/')
                messages.error(request, form.errors)
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                if Zona.objects.filter(pk=pk).count() > 0:
                    return redirect(f'/zona/{pk}/')
                else:
                    messages.error(request, "Zona no encontrada")
                    form = ZonaForm()
        else:
            form = ZonaForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            form = ZonaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/zona/')
            else:
                messages.error(request, form.errors)
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None or Zona.objects.filter(pk=pk).count() <= 0:
                messages.error(request, "Zona no encontrada")
                form = ZonaForm()
            else:
                return redirect(f'/zona/{pk}/')
    else:
        form = ZonaForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'util/form.html', context)


def RutinaView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(Rutina, id=pk)
        if request.method == 'POST':
            form = RutinaForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = RutinaForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/rutina/')
                else:
                    messages.error(request, form.errors)
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    form.save()
                    return redirect(f'/rutina/{pk}/')
                messages.error(request, form.errors)
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                if Rutina.objects.filter(pk=pk).count() > 0:
                    return redirect(f'/rutina/{pk}/')
                else:
                    messages.error(request, "Rutina no encontrada")
                    form = RutinaForm()
        else:
            form = RutinaForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            form = RutinaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/rutina/')
            else:
                messages.error(request, form.errors)
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None or Rutina.objects.filter(pk=pk).count() <= 0:
                messages.error(request, "Rutina no encontrada")
                form = RutinaForm()
            else:
                return redirect(f'/rutina/{pk}/')
    else:
        form = RutinaForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'util/form.html', context)


def PersonaView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(Persona, id=pk)
        if request.method == 'POST':
            form = PersonaForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = PersonaForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/persona/')
                else:
                    messages.error(request, form.errors)
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    form.save()
                    return redirect(f'/persona/{pk}/')
                messages.error(request, form.errors)
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                if Persona.objects.filter(pk=pk).count() > 0:
                    return redirect(f'/persona/{pk}/')
                else:
                    messages.error(request, "Persona no encontrada")
                    form = PersonaForm()
        else:
            form = PersonaForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            form = PersonaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/persona/')
            else:
                messages.error(request, form.errors)
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None or Persona.objects.filter(pk=pk).count() <= 0:
                messages.error(request, "Persona no encontrada")
                form = PersonaForm()
            else:
                return redirect(f'/persona/{pk}/')
    else:
        form = PersonaForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'util/form.html', context)


def EquipoDeEntrenamientoView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = get_object_or_404(EquipoDeEntrenamiento, id=pk)
        if request.method == 'POST':
            form = EquipoDeEntrenamientoForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = EquipoDeEntrenamientoForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/equipo/')
                else:
                    messages.error(request, form.errors)
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    form.save()
                    return redirect(f'/equipo/{pk}/')
                messages.error(request, form.errors)
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                if EquipoDeEntrenamiento.objects.filter(pk=pk).count() > 0:
                    return redirect(f'/equipo/{pk}/')
                else:
                    messages.error(
                        request, "Equipo De Entrenamiento no encontrado")
                    form = EquipoDeEntrenamientoForm()
        else:
            form = EquipoDeEntrenamientoForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            form = EquipoDeEntrenamientoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/equipo/')
            else:
                messages.error(request, form.errors)
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None or EquipoDeEntrenamiento.objects.filter(pk=pk).count() <= 0:
                messages.error(
                    request, "Equipo De Entrenamiento no encontrado")
                form = EquipoDeEntrenamientoForm()
            else:
                return redirect(f'/equipo/{pk}/')
    else:
        form = EquipoDeEntrenamientoForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'util/form.html', context)


def Home(request):

    return render(request, 'home/home.html')
