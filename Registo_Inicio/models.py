from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Cada modelo representa una tabla, cada vez que se instancia un modelo este


# Entidad que representa la publicacion de una inmobiliaria.
class PublicacionInmobiliaria(models.Model):
    # Atributo titulo
    titulo = models.CharField(max_length=100)
    # Atributo  fecha
    fecha = models.DateField(default="2005/08/09") 
    # Atributo precio
    precio = models.IntegerField(default=0)
    # Atributo descripcion
    descripcion = models.TextField(default=0)
    # Atributo imagens
    imagenes = models.ImageField(blank=True)
    # Atributo usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "Publicacion_guardada_Usuario", default= None)
    # prueba = models.CharField(max_length=100)

    # Metodo magico para mostrar el titulo
    def __str__(self) -> str:
        return self.titulo
    

    