from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.admin import widgets


class ClaseForm(ModelForm):
    equipos_de_entrenamiento = forms.ModelMultipleChoiceField(EquipoDeEntrenamiento.objects.all(
    ), widget=widgets.FilteredSelectMultiple("EquipoDeEntrenamiento", False, attrs={'rows': '2'}), required=False)

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
    class Meta:
        model = Calendario
        fields = '__all__'


class ZonaForm(ModelForm):
    class Meta:
        model = Zona
        fields = '__all__'


class RutinaForm(ModelForm):
    class Meta:
        model = Rutina
        fields = '__all__'


class PersonaForm(ModelForm):
    clases = forms.ModelMultipleChoiceField(Clase.objects.all(
    ), widget=widgets.FilteredSelectMultiple("Clase", False, attrs={'rows': '2'}), required=False)

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
    class Meta:
        model = EquipoDeEntrenamiento
        fields = '__all__'
