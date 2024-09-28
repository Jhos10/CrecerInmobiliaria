from django.shortcuts import render, redirect
from django.http import HttpResponse
from Registo_Inicio.models import PublicacionInmobiliaria, ImagenPublicacion
# Create your views here.

def paginaPrincipal(request):
    publicaciones = PublicacionInmobiliaria.objects.all()
    # contexto = {"publicaciones": publicaciones}
    if not publicaciones:
        print("Hola")
        contexto = {"publicaciones": None}
    else:
        print("Inagresa el else")
        contexto = {"publicaciones": publicaciones}
    return render(request, "paginaPrincipal.html", contexto)

def publicacion(request, idPublicacion):
    try:
        publicacion = PublicacionInmobiliaria.objects.get(id = idPublicacion)
        imagenes = publicacion.imagenpublicacion_set.all()
        # imagenes = list(map(lambda x: x.imagen.url, imagenes))
        # imagenes += [publicacion.imagenPrincipal.url]
        # print(imagenes)
        # except

        return render(request,'publicacion.html', {
            'publicacion': publicacion,
            'imagenes': imagenes
        })
    except PublicacionInmobiliaria.DoesNotExist:
        return HttpResponse("La publicacion no existe")


