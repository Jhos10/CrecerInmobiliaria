from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PublicacionInmobiliaria(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(default="2005/08/09") 
    precio = models.IntegerField(default=0)
    descripcion = models.TextField(default=0)
    imagenes = models.ImageField(blank=True)
    # prueba = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.titulo
    