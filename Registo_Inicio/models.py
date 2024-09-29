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
    imagenPrincipal = models.ImageField(upload_to='static/images/', default=None)
    
    # imagenes = models.
    # Atributo usuario    # prueba = models.CharField(max_length=100)

    # Metodo magico para mostrar el titulo
    def __str__(self) -> str:
        return self.titulo

class ImagenPublicacion(models.Model):
    publicacionInmobiliaria = models.ForeignKey(PublicacionInmobiliaria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='static/images/')

class VideoPublicacion(models.Model):
    publicacionInmobiliaria = models.ForeignKey(PublicacionInmobiliaria, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to='static/videosPublicaciones')

class User_PublicacionInmobiliaria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacionInmobiliaria = models.ForeignKey(PublicacionInmobiliaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username, self.publicacionInmobiliaria.titulo
    

    