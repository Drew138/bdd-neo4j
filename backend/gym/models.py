from neomodel import (
    StringProperty,
    IntegerProperty,
    DateTimeProperty,
    DateProperty,
    JSONProperty,
    Relationship
)
from django_neomodel import DjangoNode
from .choices import *

class Calendario(DjangoNode):
    # uid = UniqueIdProperty()
    dia = StringProperty()

    fecha_inicio = DateProperty()
    fecha_final = DateProperty()

    class Meta:
        app_label = 'gym'

    def __str__(self):
         return f"Dia:{self.dia} - entre {self.fecha_inicio} y {self.fecha_final}"

class Zona(DjangoNode):
    piso = StringProperty()
    tipo = StringProperty()
    class Meta:
        app_label = 'gym'
    
    def __str__(self):
        return f"{self.piso} piso - {self.tipo}"

class EquipoDeEntrenamiento(DjangoNode):
    nombre = StringProperty()
    grupo_muscular = StringProperty()
    zona = Relationship(Zona, "tiene")
    fecha_mantemiento = DateProperty()
    fecha_adquisicion = DateProperty()
    marca = StringProperty()
    cantidad = IntegerProperty()
    class Meta:
        app_label = 'gym'

    def __str__(self):
         return f"Maquina de {self.grupo_muscular} - Zona:{self.zona} - Adquisicion {self.fecha_adquisicion} - {self.cantidad} en inventario"


class Rutina(DjangoNode):
    grupo_muscular = StringProperty()
    cantidad_ejercicios = IntegerProperty()
    dificultad = StringProperty()
    repeticiones = IntegerProperty()
    lista_equipos = JSONProperty()
    class Meta:
        app_label = 'gym'

    def __str__(self):
         return f"{self.grupo_muscular} - {self.cantidad_ejercicios} ejercicios por {self.repeticiones} repeticiones - {self.dificultad}"


class Clase(DjangoNode):
    nombre = StringProperty()
    tipo = StringProperty()
    costo = IntegerProperty()
    zona = Relationship(Zona, "tiene")
    rutina = Relationship("Rutina", "tiene")
    maximo_personas = IntegerProperty()
    calendario = Relationship("Calendario", "tiene")
    equipos_de_entrenamiento = Relationship("EquipoDeEntrenamiento", "tiene")
    class Meta:
        app_label = 'gym'


    def __str__(self):
         return f"Clase de {self.tipo} - Costo: {self.costo} - Ubicacion:{self.zona} - Rutina:{self.rutina} - Max:{self.maximo_personas} personas - Calendario:{self.calendario} - Equipos Entrenamiento:{self.equipos_de_entrenamiento}"

    

class Persona(DjangoNode):
    nombre = StringProperty()
    tipo = StringProperty()
    sexo = StringProperty()
    plan_de_pago = StringProperty()
    remuneracion = IntegerProperty()
    clases = Relationship("Clase", "tiene")
    class Meta:
        app_label = 'gym'

    def __str__(self):
         return f"Nombre:{self.nombre} - {self.tipo} - Genero:{self.sexo} - Plan:{self.plan}"


# class Calendario(models.Model):  # TODO
#     dia = models.CharField(
#         max_length=255, choices=DiasEnum.choices, null=False, blank=False)  # enum
#     hora_inicial = models.TimeField(null=False, blank=False)
#     hora_final = models.TimeField(null=False, blank=False)
#     fecha_inicio = models.DateField(null=False, blank=False)
#     fecha_final = models.DateField(null=False, blank=False)

#     def __str__(self):
#         return f"Dia:{self.dia} - entre {self.fecha_inicio} y {self.fecha_final} - Hora:{self.hora_inicial} hasta {self.hora_final}"


# class Zona(models.Model):

#     piso = models.CharField(
#         max_length=255, choices=PisosEnum.choices, null=False, blank=False)  # enum
#     tipo = models.CharField(
#         max_length=255, choices=TipoZonasEnum.choices, null=False, blank=False)  # enum

#     def __str__(self):
#         return f"{self.piso} piso - {self.tipo}"


# class Rutina(models.Model):
#     grupo_muscular = models.CharField(
#         max_length=255, choices=GrupoMuscularEnum.choices, null=False, blank=False)  # enum
#     cantidad_ejercicios = models.IntegerField(null=False, blank=False)
#     dificultad = models.CharField(
#         max_length=255, choices=DificultadesEnum.choices, null=False, blank=False)  # enum
#     repeticiones = models.IntegerField(null=False, blank=False)
#     lista_equipos = models.JSONField()  # TODO

#     def __str__(self):
#         return f"{self.grupo_muscular} - {self.cantidad_ejercicios} ejercicios por {self.repeticiones} repeticiones - {self.dificultad}"


# class Persona(models.Model):

#     nombre = models.CharField(max_length=255, null=False, blank=False)
#     tipo = models.CharField(
#         max_length=255, choices=TipoPersonaEnum.choices, null=False, blank=False)  # enum
#     sexo = models.CharField(
#         max_length=255, choices=SexoEnum.choices, null=False, blank=False)  # enum
#     plan = models.CharField(
#         max_length=255, choices=PlanPagoEnum.choices, null=False, blank=False)  # enum
#     remuneracion = models.IntegerField(default=0)
#     clases = models.ManyToManyField(
#         'Clase', blank=True)

#     def __str__(self):
#         return f"Nombre:{self.nombre} - {self.tipo} - Genero:{self.sexo} - Plan:{self.plan}"


# class EquipoDeEntrenamiento(models.Model):

#     nombre = models.CharField(max_length=255, null=False, blank=False)
#     grupo_muscular = models.CharField(
#         max_length=255, choices=GrupoMuscularEnum.choices, null=False, blank=False)  # enum
#     zona = models.ForeignKey(
#         'Zona', null=True, blank=True, on_delete=models.SET_NULL)
#     fecha_mantemiento = models.DateField(null=False, blank=False)
#     fecha_adquisicion = models.DateField(null=False, blank=False)
#     marca = models.CharField(max_length=255, null=False, blank=False)
#     cantidad = models.IntegerField(null=False, blank=False)

#     def __str__(self):
#         return f"Maquina de {self.grupo_muscular} - Zona:{self.zona} - Adquisicion {self.fecha_adquisicion} - {self.cantidad} en inventario"


# class Clase(models.Model):
#     nombre = models.CharField(max_length=255, null=False, blank=False)
#     tipo = models.CharField(
#         max_length=255, choices=TiposDeClaseEnum.choices, null=False, blank=False)  # enum
#     costo = models.IntegerField(default=0)
#     zona = models.ForeignKey(
#         'Zona', null=True, blank=True, on_1delete=models.SET_NULL)
#     rutina = models.ForeignKey(
#         'Rutina', null=False, blank=False, on_delete=models.CASCADE)
#     maximo_personas = models.IntegerField(null=False, blank=False)
#     calendario = models.ForeignKey(
#         'Calendario', null=False, blank=False, on_delete=models.CASCADE)
#     equipos_de_entrenamiento = models.ManyToManyField(
#         'EquipoDeEntrenamiento', blank=True)

#     def __str__(self):
#         return f"Clase de {self.tipo} - Costo: {self.costo} - Ubicacion:{self.zona} - Rutina:{self.rutina} - Max:{self.maximo_personas} personas - Calendario:{self.calendario} - Equipos Entrenamiento:{self.equipos_de_entrenamiento}"
