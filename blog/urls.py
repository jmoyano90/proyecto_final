from django import views
from django.contrib import admin
from django.urls import path, include

from blog.views import (
    buscar_autor,
    buscar_seccion,
    busqueda_articulo,
    busqueda_seccion,
    mostrar_inicio,
    procesar_fomulario_articulo,
    procesar_fomulario_seccion,
    procesar_fomulario_autor,
    busqueda_autor,
    busqueda_articulo,
    busqueda_seccion,
    buscar_articulo,
)


urlpatterns = [
    path('inicio/', mostrar_inicio),
    path('formulario-articulo/', procesar_fomulario_articulo),
    path('formulario-seccion/', procesar_fomulario_seccion),
    path('formulario-autor/', procesar_fomulario_autor),
    path('busqueda_autor/', busqueda_autor),
    path('busqueda_articulo/', busqueda_articulo),
    path('busqueda_seccion/', busqueda_seccion),
    path('buscar_articulo/', buscar_articulo),
    path('buscar_autor/', buscar_autor),
    path('buscar_seccion/', buscar_seccion),
]
