from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('clase/', views.ClaseView, name='clases'),
    path('clase/<pk>/', views.ClaseView, name='clases-pk'),
    path('calendario/', views.CalendarioView, name='calendario'),
    path('calendario/<pk>/', views.CalendarioView, name='calendario-pk'),
    path('zona/', views.ZonaView, name='zona'),
    path('zona/<pk>/', views.ZonaView, name='zona-pk'),
    path('rutina/', views.RutinaView, name='rutina'),
    path('rutina/<pk>/', views.RutinaView, name='rutina-pk'),
    path('persona/', views.PersonaView,
         name='persona'),
    path('persona/<pk>/', views.PersonaView,
         name='persona-pk'),
    path('equipo/', views.EquipoDeEntrenamientoView,
         name='equipo'),
    path('equipo/<pk>/', views.EquipoDeEntrenamientoView,
         name='equipo-pk'),
]
