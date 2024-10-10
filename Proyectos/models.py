from django.db import models

# Create your models here.
class Proyect(models.Model):
  tituloProyecto = models.CharField(max_length=100, default='No tiene nombre')
  precio = models.BigIntegerField(default=0)
  ubicacion = models.CharField(max_length=100, default='No se especifica la ubicacion')
  descripcion = models.TextField(max_length=100, default='No tiene una descripcion')
  proyectoImagenPrincipal = models.ImageField(default="No tiene imagenes", upload_to='static/proyectoImages/')

class ImagenesProyectos(models.Model):
  proyecto = models.ForeignKey(Proyect, on_delete= models.CASCADE)
  imagenProyecto = models.ImageField(upload_to='static/proyectoImages/')

class VideoProyectos(models.Model):
  proyecto = models.ForeignKey(Proyect, on_delete= models.CASCADE)
  videoProyecto = models.FileField(upload_to='static/videosProyectos/')



