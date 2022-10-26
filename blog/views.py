from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Articulo, Autor, Seccion
from blog.forms import ArticuloForm, AutorForm, SeccionForm


def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_fomulario_articulo(request):

    if request.method == "GET":
        mi_formulario = ArticuloForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-articulo.html", context=contexto)

    if request.method == "POST":

        mi_formulario = ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo=datos_ingresados_por_usuario["titulo"],
                texto=datos_ingresados_por_usuario["texto"],
                fecha=datos_ingresados_por_usuario["fecha"],
            )
        nuevo_modelo.save()

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-articulo.html", context=contexto)


def procesar_fomulario_seccion(request):

    if request.method == "GET":
        mi_formulario = SeccionForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-seccion.html", context=contexto)

    if request.method == "POST":

        mi_formulario = SeccionForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Seccion(
                nombre=datos_ingresados_por_usuario["nombre"],
            )
        nuevo_modelo.save()

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-seccion.html", context=contexto)


def procesar_fomulario_autor(request):

    if request.method == "GET":
        mi_formulario = AutorForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-autor.html", context=contexto)

    if request.method == "POST":
        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autor(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
                profesion=datos_ingresados_por_usuario["profesion"],
            )
        nuevo_modelo.save()

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-autor.html", context=contexto)

def busqueda_autor(request):
    return render(request, "blog/busqueda_autor.html")

def busqueda_articulo(request):
    return render(request, "blog/busqueda_articulo.html")

def busqueda_seccion(request):
    return render(request, "blog/busqueda_seccion.html")

def buscar_articulo(request):
    respuesta = f"Estoy buscando el articulo: {request.GET['articulo']}"
    return HttpResponse(respuesta)

def buscar_autor(request):
    respuesta = f"Estoy buscando el autor: {request.GET['autor']}"
    return HttpResponse(respuesta)

def buscar_seccion(request):
    respuesta = f"Estoy buscando la seccion: {request.GET['seccion']}"
    return HttpResponse(respuesta)

def busqueda_autor(request):
    return render(request, "blog/busqueda_de_autor.html")

def buscar_autor(request):
    if not request.GET["Autor"]:
        return HttpResponse("No enviaste datos")
    else:
        autor_a_buscar = request.GET["Autor"]
        autores = Autor.objects.filter(nombre=autor_a_buscar)
        
        contexto = {
            "Autor": autor_a_buscar,
            "autores_encontrados": autores
        }
        
        return render(request, "blog/busqueda_autor.html", contexto)

def buscar_articulo(request):
    if not request.GET["Articulo"]:
        return HttpResponse("No enviaste datos")
    else:
        articulo_a_buscar = request.GET["Articulo"]
        articulos = Articulo.objects.filter(titulo=articulo_a_buscar)
        
        contexto = {
            "Articulo": articulo_a_buscar,
            "articulos_encontrados": articulos
        }
        
        return render(request, "blog/busqueda_articulo.html", contexto)
    
def buscar_seccion(request):
    if not request.GET["Seccion"]:
        return HttpResponse("No enviaste datos")
    else:
        seccion_a_buscar = request.GET["Seccion"]
        secciones = Seccion.objects.filter(nombre=seccion_a_buscar)
        
        contexto = {
            "Seccion": seccion_a_buscar,
            "secciones_encontrados": secciones
        }
        
        return render(request, "blog/busqueda_seccion.html", contexto)