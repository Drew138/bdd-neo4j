from django.db import models


class DiasEnum(models.TextChoices):
    lunes = 'lunes', 'Lunes'
    martes = 'martes', 'Martes'
    miercoles = 'miercoles', 'Miercoles'
    jueves = 'jueves', 'Jueves'
    viernes = 'viernes', 'Viernes'
    sabado = 'sabado', 'Sabado'
    domingo = 'domingo', 'Domingo'


class DificultadesEnum(models.TextChoices):
    inicial = 'inicial', 'Inicial'
    intermedio = 'intermedio', 'Intermedio'
    avanzado = 'Avanzado', 'Avanzado'


class PisosEnum(models.TextChoices):
    primero = 'primero', 'Primero'
    segundo = 'segundo', 'Segundo'
    tercero = 'tercero', 'Tercero'
    cuarto = 'cuarto', 'Cuarto'


class GrupoMuscularEnum(models.TextChoices):
    pecho = 'pecho', 'Pecho'
    hombro = 'hombro', 'Hombro'
    triceps = 'triceps', 'Triceps'
    biceps = 'biceps', 'Biceps'
    espalda = 'espalda', 'Espalda'
    trapecio = 'trapecio', 'Trapecio'
    abdomen = 'abdomen', 'Abdomen'
    isquiotibiales = 'isquiotibiales', 'Isquiotibiales'
    cuadriceps = 'cuadriceps', 'Cuadriceps'
    gluteos = 'gluteos', 'Gluteos'


class TipoPersonaEnum(models.TextChoices):
    entrenador = 'entrenador', 'Entrenador'
    cliente = 'cliente', 'Cliente'
    mantenimiento = 'mantenimiento', 'Mantenimiento'
    servicios_varios = 'servicios varios', 'Servicios varios'
    recepcion = 'recepcion', 'Recepcion'


class PlanPagoEnum(models.TextChoices):
    dia = 'dia', 'Dia'
    mes = 'mes', 'Mes'
    trimestral = 'trimestral', 'Trimestral'
    semestral = 'semestral', 'Semestral'
    anual = 'anual', 'Anual'


class SexoEnum(models.TextChoices):
    masculino = 'masculino', 'Masculino'
    femenino = 'femenino', 'Femenino'


class TipoZonasEnum(models.TextChoices):
    musculacion = 'musculacion', 'Musculacion'
    cardio = 'cardio', 'Cardio'


class TiposDeClaseEnum(models.TextChoices):
    yoga = 'yoga', 'Yoga'
    fuerza = 'fuerza', 'Fuerza'
    cardio = 'cardio', 'Cardio'
    danza = 'danza', 'Danza'
    zumba = 'zumba', 'Zumba'
