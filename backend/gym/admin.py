from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Calendario)
class CalendarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Rutina)
class RutinaAdmin(admin.ModelAdmin):
    pass


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'tipo', 'sexo', 'plan', 'remuneracion']
    list_filter = ['id', 'nombre', 'tipo', 'sexo', 'plan', 'remuneracion']
    list_display = ['nombre', 'tipo', 'sexo', 'plan', 'remuneracion']


# @admin.register(RegistroDeClase)
# class RegistroDeClaseAdmin(admin.ModelAdmin):
#     pass


@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    pass


@admin.register(EquipoDeEntrenamiento)
class EquipoDeEntrenamientoAdmin(admin.ModelAdmin):
    pass


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    pass
