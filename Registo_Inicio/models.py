from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Cada modelo representa una tabla, cada vez que se instancia un modelo este
# Clase que define las opciones que puede tener alguna campo de otra clase, en este caso se estan poniendo las opciones de 
class TipoInmueble(models.TextChoices):
    casa = 'Casa'
    apartamento = 'Apartamento'


# Entidad que representa la publicacion de una inmobiliaria.
class PublicacionInmobiliaria(models.Model):
    # Atributos de la clase
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(default="2005/08/09") 
    precio = models.IntegerField(default=0)
    descripcion = models.TextField(default=0)
    imagenPrincipal = models.ImageField(upload_to='static/images/', default=None)
    tipoInmueble = models.CharField(default=TipoInmueble.casa, choices=TipoInmueble.choices, max_length = 50)
    numeroCamas = models.IntegerField(default=0)
    numeroBaños = models.IntegerField(default=0)
    tamaño = models.IntegerField(default=0)
    numeroDormitorios = models.IntegerField(default=0)

    # Metodo magico para mostrar el titulo
    def __str__(self) -> str:
        return self.titulo

class ImagenPublicacion(models.Model):
    # Atributos de la clase
    publicacionInmobiliaria = models.ForeignKey(PublicacionInmobiliaria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='static/images/')

class VideoPublicacion(models.Model):
    # Atributos de la clase
    publicacionInmobiliaria = models.ForeignKey(PublicacionInmobiliaria, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to='static/videosPublicaciones')

class User_PublicacionInmobiliaria(models.Model):
    # Atributos de la clase
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacionInmobiliaria = models.ForeignKey(PublicacionInmobiliaria, on_delete=models.CASCADE)

    # Metodo magico para que muestre en consola el usuario y el titulo de la publicacion si se imprime alguna instancia de la clase
    def __str__(self):
        return self.usuario.username, self.publicacionInmobiliaria.titulo
    

    