from django.db import models

# Create your models here.
class Proyect(models.Model):
  # Atributos de clase que representan la entidad Proyect
  tituloProyecto = models.CharField(max_length=100, default='No tiene nombre')
  precio = models.BigIntegerField(default=0)
  ubicacion = models.CharField(max_length=100, default='No se especifica la ubicacion')
  descripcion = models.TextField(max_length=4000, default='No tiene una descripcion')
  proyectoImagenPrincipal = models.ImageField(default="No tiene imagenes", upload_to='static/proyectoImages/')
  logo = models.ImageField(default="No tiene icono", upload_to='static/proyectoImages/')
  acabados = models.TextField(max_length=500,default='No tiene descripcion')

  # Metodo str para ver el titulo del proyecto en la consola y en el panel de admin
  def __str__(self) -> str:
    return self.tituloProyecto
    
class ImagenesProyectos(models.Model):
  proyecto = models.ForeignKey(Proyect, on_delete= models.CASCADE)
  imagenProyecto = models.ImageField(upload_to='static/proyectoImages/')
  # Metodo str para ver el id del proyecto
  def __str__(self) -> str:
    return str(self.proyecto)
  
class PlanosProyectos(models.Model):
  proyecto = models.ForeignKey(Proyect, on_delete= models.CASCADE)
  planosImagenes = models.ImageField(default='No tiene planos', upload_to='static/proyectoImages/')
  # Metodo str para vel id del proyecto
  # def __str__(self) -> str:
  #   return self.proyecto.pk
  def __str__(self) -> str:
    return str(self.proyecto)


class VideoProyectos(models.Model):
  proyecto = models.ForeignKey(Proyect, on_delete= models.CASCADE)
  videoProyecto = models.FileField(upload_to='static/videosProyectos/')
  

  def __str__(self) -> str:
    return str(Proyect)


