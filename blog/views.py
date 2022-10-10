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

def busqueda(request):
    return render(request, "blog/busqueda.html")

def busqueda_2(request):
    return render(request, "blog/busqueda_2.html")

def buscar(request):
    respuesta = f"Estoy buscando el articulo: {request.GET['articulo']}"
    
def buscar_2(request):
    if not request.GET['articulo']:
        return HttpResponse("No se encuentra ese articulo, por favor busca otro")
    else:
        articulo = request.GET['articulo']
        producto = producto.objects.filter(articulo=articulo)
        
    contexto = {
        "articulo": articulo,
        "producto_encontrado": producto,
    }
    
    return render(request, "blog/resultado_busqueda.html", contexto)