from django import views
from django.contrib import admin
from django.urls import path, include

from blog.views import (
    mostrar_inicio,
    procesar_fomulario_articulo,
    procesar_fomulario_seccion,
    procesar_fomulario_autor,
    busqueda,
    buscar,
)


urlpatterns = [
    path('inicio/', mostrar_inicio),
    path('formulario-articulo/', procesar_fomulario_articulo),
    path('formulario-seccion/', procesar_fomulario_seccion),
    path('formulario-autor/', procesar_fomulario_autor),
    path('busqueda/', busqueda),
    path('buscar/', buscar),

]
