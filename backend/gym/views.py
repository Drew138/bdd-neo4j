from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

def connection_helper(table, form, related_model):
    # print(form['zona'].value())
    instance = table(id=int(form[related_model].value()))
    instance.refresh()
    return instance

def connection_helper_many_to_many(table, form, related_model):
    sol = []
    for key in form[related_model].value():
        instance = table(id=int(key))
        instance.refresh()
        sol.append(instance)
    return sol

def search_model_instance(model, id):
    objects = model.nodes.all()
    for instance in objects:
        if instance.id == int(id):
            return instance
    return None


def ClaseView(request, *args, **kwargs):
    if 'pk' in kwargs:
        pk = kwargs['pk']
        instance = search_model_instance(Clase, pk)
        if not instance:
            raise Exception('404 Alejo es gay')
        if request.method == 'POST':
            form = ClaseForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = ClaseForm(request.POST)
                if form.is_valid():
                    clase1 = form.save()
                    clase1.zona.connect(connection_helper(Zona, form, 'zona'))
                    clase1.calendario.connect(connection_helper(Calendario, form, 'calendario'))
                    clase1.rutina.connect(connection_helper(Rutina, form, 'rutina'))
                    for equipo in connection_helper_many_to_many(EquipoDeEntrenamiento, form, "equipos_de_entrenamiento"):
                        clase1.equipos_de_entrenamiento.connect(equipo)
                    return redirect('/clase/')
                else:
                    messages.error(request, form.errors)
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    clase1 = form.save()
                    clase1.zona.disconnect_all()
                    clase1.calendario.disconnect_all()
                    clase1.rutina.disconnect_all()
                    clase1.equipos_de_entrenamiento.disconnect_all()
                    clase1.zona.connect(connection_helper(Zona, form, 'zona'))
                    clase1.calendario.connect(connection_helper(Calendario, form, 'calendario'))
                    clase1.rutina.connect(connection_helper(Rutina, form, 'rutina'))
                    for equipo in connection_helper_many_to_many(EquipoDeEntrenamiento, form, "equipos_de_entrenamiento"):
                        clase1.equipos_de_entrenamiento.connect(equipo)
                    return redirect(f'/clase/{pk}/')
                messages.error(request, form.errors)
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                if search_model_instance(Clase, pk) != None:
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
                clase1 = form.save()
                clase1.zona.connect(connection_helper(Zona, form, 'zona'))
                clase1.calendario.connect(connection_helper(Calendario, form, 'calendario'))
                clase1.rutina.connect(connection_helper(Rutina, form, 'rutina'))
                for equipo in connection_helper_many_to_many(EquipoDeEntrenamiento, form, "equipos_de_entrenamiento"):
                    clase1.equipos_de_entrenamiento.connect(equipo)

                return redirect('/clase/')
            else:
                messages.error(request, form.errors)
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None or search_model_instance(Clase, pk) == None:
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
        instance = search_model_instance(Calendario, pk)
        if instance == None: 
            raise Exception('404 alejo es gay')
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
                if search_model_instance(Calendario, pk) != None:
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
            # print(search_model_instance(Calendario, pk))
            if pk is None or search_model_instance(Calendario, pk) == None:
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
        instance = search_model_instance(Zona, pk)
        if not instance:
            raise Exception('404 Alejo es gay')
        if not instance:
            raise Exception('404 Alejo es gay')
        if request.method == 'POST':
            form = ZonaForm(request.POST, instance=instance)
            print(request.POST)
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

                if pk is None or search_model_instance(Zona, pk) == None:
                    messages.error(request, "Zona no encontrada")
                    form = ZonaForm()
                
                else:
                    return redirect(f'/zona/{pk}/')
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
            if pk is None or search_model_instance(Zona, pk) == None:
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
        instance = search_model_instance(Rutina, pk)
        if not instance:
            raise Exception('404 Alejo es gay')
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
                if search_model_instance(Rutina, pk) != None:
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
            if pk is None or search_model_instance(Rutina, pk) == None:
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
        instance = search_model_instance(Persona, pk)
        if not instance:
            raise Exception('404 Alejo es gay')

        if request.method == 'POST':
            form = PersonaForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = PersonaForm(request.POST)
                if form.is_valid():
                    persona1 = form.save()
                    for clase in connection_helper_many_to_many(Clase, form, "clase"):
                        persona1.clases.connect(clase)
                    return redirect('/persona/')
                else:
                    messages.error(request, form.errors)
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    persona1 = form.save()
                    persona1.clases.disconnect_all()
                    for clase in connection_helper_many_to_many(Clase, form, "clases"):
                        persona1.clases.connect(clase)
                    return redirect(f'/persona/{pk}/')
                messages.error(request, form.errors)
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                if search_model_instance(Persona, pk) != None:
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
                persona1 = form.save()
                for clase in connection_helper_many_to_many(Clase, form, "clases"):
                        persona1.clases.connect(clase)
                return redirect('/persona/')
            else:
                messages.error(request, form.errors)
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None or search_model_instance(Persona, pk) == None:
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
        instance = search_model_instance(EquipoDeEntrenamiento, pk)
        if not instance:
            raise Exception('404 Alejo es gay')
        if request.method == 'POST':
            form = EquipoDeEntrenamientoForm(request.POST, instance=instance)
            if 'crear' in request.POST:
                form = EquipoDeEntrenamientoForm(request.POST)
                if form.is_valid():
                    nodo_zona = EquipoDeEntrenamiento.nodes.filter(id=form['fields']['id'])
                    equipo1 = form.save()
                    equipo1.zona.connect(connection_helper(Zona, form, 'zona'))
                    return redirect('/equipo/')
                else:
                    messages.error(request, form.errors)
            elif 'borrar' in request.POST:
                instance.delete()
                return redirect('/')
            elif 'actualizar' in request.POST:
                if form.is_valid():
                    equipo1 = form.save()
                    equipo1.zona.disconnect_all()
                    equipo1.zona.connect(connection_helper(Zona, form, 'zona'))
                    return redirect(f'/equipo/{pk}/')
                messages.error(request, form.errors)
            elif 'buscar' in request.POST:
                pk = request.POST.get('primary_key', None) or pk
                if search_model_instance(EquipoDeEntrenamiento, pk) != None:
                    return redirect(f'/equipo/{pk}/')
                else:
                    messages.error(request, "EquipoEntrenamiento no encontrada")
                    form = EquipoDeEntrenamientoForm()
        else:
            form = EquipoDeEntrenamientoForm(instance=instance)
    elif request.method == 'POST':
        if 'crear' in request.POST:
            form = EquipoDeEntrenamientoForm(request.POST)
            if form.is_valid():
                equipo1 = form.save()
                equipo1.zona.connect(connection_helper(Zona, form, 'zona'))
                
                return redirect('/equipo/')
            else:
                messages.error(request, form.errors)
        elif 'buscar' in request.POST:
            pk = request.POST.get('primary_key')
            if pk is None or search_model_instance(EquipoDeEntrenamiento, pk) == None:
                messages.error(request, "EquipoEntrenamiento no encontrada")
                form = EquipoDeEntrenamientoForm()
            else:
                return redirect(f'/equipo/{pk}/')
    else:
        form = EquipoDeEntrenamientoForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'util/form.html', context)


def Home(request):

    return render(request, 'home/home.html')
