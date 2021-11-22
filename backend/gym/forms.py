from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.admin import widgets
from .choices import *

def get_zonas():
    return ((zona.id, str(zona)) for zona in Zona.nodes.all())

def get_equipos_de_entrenamiento():
    return ((equipo.id, str(equipo)) for equipo in EquipoDeEntrenamiento.nodes.all())

def get_rutinas():
    return ((rutina.id, str(rutina)) for rutina in Rutina.nodes.all())

def get_calendarios():
    return ((calendario.id, str(calendario)) for calendario in Calendario.nodes.all())

def get_clases():
    return ((clase.id, str(clase)) for clase in Clase.nodes.all())

class ClaseForm(ModelForm):
    tipo = forms.ChoiceField(widget=forms.Select(), choices=TiposDeClaseEnum)
    zona = forms.ChoiceField(
        widget=forms.Select(),
        choices=get_zonas
    )
    rutina = forms.ChoiceField(
        widget=forms.Select(),
        choices=get_rutinas
    )
    calendario = forms.ChoiceField(
        widget=forms.Select(),
        choices= get_calendarios
    )
    equipos_de_entrenamiento = forms.MultipleChoiceField(
        choices=get_equipos_de_entrenamiento, 
        widget=widgets.FilteredSelectMultiple("EquipoDeEntrenamiento", False, attrs={'rows': '2'}), 
        required=False
    )
    class Meta:
        model = Clase
        fields = '__all__'
        css = {
            'all': ('/static/admin/css/widgets.css',),
        }
        js = ('/admin/jsi18n',)

    def clean_drg_choise(self):
        drg_choise = self.cleaned_data['drg_choise']
        return drg_choise


class CalendarioForm(ModelForm):

    dia = forms.ChoiceField(widget=forms.Select(), choices=DiasEnum, required=True)
    class Meta:
        model = Calendario
        fields = '__all__'


class ZonaForm(ModelForm):
    piso = forms.ChoiceField(widget=forms.Select(), choices=PisosEnum)
    tipo = forms.ChoiceField(widget=forms.Select(), choices=TipoZonasEnum)
    class Meta:
        model = Zona
        fields = '__all__'


class RutinaForm(ModelForm):
    grupo_muscular = forms.ChoiceField(widget=forms.Select(), choices=GrupoMuscularEnum)
    dificultad = forms.ChoiceField(widget=forms.Select(), choices=DificultadesEnum)
    class Meta:
        model = Rutina
        fields = '__all__'


class PersonaForm(ModelForm):
    tipo = forms.ChoiceField(widget=forms.Select(), choices=TipoPersonaEnum)
    sexo = forms.ChoiceField(widget=forms.Select(), choices=SexoEnum)
    plan_de_pago = forms.ChoiceField(widget=forms.Select(), choices=PlanPagoEnum)
    clases = forms.MultipleChoiceField(
        choices=get_clases, 
        widget=widgets.FilteredSelectMultiple("Clase", False, attrs={'rows': '2'}), 
        required=False
    )
    class Meta:
        model = Persona
        fields = '__all__'
        css = {
            'all': ('/static/admin/css/widgets.css',),
        }
        js = ('/admin/jsi18n',)

    def clean_drg_choise(self):
        drg_choise = self.cleaned_data['drg_choise']
        return drg_choise


class EquipoDeEntrenamientoForm(ModelForm):
    grupo_muscular = forms.ChoiceField(widget=forms.Select(), choices=GrupoMuscularEnum, required=True)
    
    zona = forms.ChoiceField(
        widget=forms.Select(),

        choices=get_zonas,
    )

    # def __init__(self):
    #     print([(zona.id, str(zona)) for zona in Zona.objects.all()])

    class Meta:
        model = EquipoDeEntrenamiento
        fields = '__all__'