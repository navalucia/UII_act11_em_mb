# miembros/urls.py (Aplicación)

from django.urls import path
from . import views # La importación relativa sigue funcionando
 
app_name = 'app_miembros'

urlpatterns = [
    # RUTA DE INICIO (maneja la URL base: /)
    path('', views.index, name='inicio'),
    
    # Rutas de Membresías
    path('membresias/', views.lista_membresias, name='lista_membresias'),
    path('membresias/agregar/', views.crear_membresia, name='agregar_membresia'),
    path('membresias/modificar/<int:id_membresia>/', views.editar_membresia, name='modificar_membresia'),
    path('membresias/eliminar/<int:id_membresia>/', views.editar_membresia, name='eliminar_membresia'),
    # Rutas de Miembros
    path('miembros/', views.lista_miembros, name='lista_miembros'),
    path('miembros/agregar/', views.crear_miembro, name='agregar_miembro'),
    path('miembros/modificar/<int:id_miembro>/', views.editar_miembro, name='modificar_miembro'),
    path('miembros/eliminar/<int:id_miembro>/', views.editar_miembro, name='eliminar_miembro'),
]