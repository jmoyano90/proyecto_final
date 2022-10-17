from pyexpat import model
from django.db import models

# Create your models here.
class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, null=True)
    profesion = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"({self.nombre}) {self.apellido}"


class Articulo(models.Model):
    class Meta:
        verbose_name_plural = "Articulos"

    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=1000)
    fecha = models.DateTimeField(null=True)

    def __str__(self):
        return self.titulo


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"

    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
