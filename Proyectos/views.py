from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse

# Create your views here.

def proyectos(request):
  proyectos = Proyect.objects.all()
  if not proyectos:
    return render(request, 'proyectos.html', {'proyectos': None})
  else:
    return render(request, 'proyectos.html', {
      'proyectos': proyectos
    })

def proyecto(request, idProyecto):
  try:
    proyecto = get_object_or_404(Proyect,id = idProyecto)
    imagenesProyecto = proyecto.imagenesproyectos_set.all()
    return render(request, 'proyecto.html', {
      'proyecto': proyecto,
      'imagenesProyecto': imagenesProyecto
    })
  except Proyect.DoesNotExist:
    return HttpResponse('No existe el proyecto.')