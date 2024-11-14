from django.shortcuts import render, redirect
from django.http import HttpResponse
from Registo_Inicio.models import PublicacionInmobiliaria, ImagenPublicacion
from django.db.models import Q
from django.views.decorators.cache import never_cache
# Create your views here.
# @never_cache
def paginaPrincipal(request):
    publicaciones = PublicacionInmobiliaria.objects.all()
    # contexto = {"publicaciones": publicaciones}
    if request.method == 'GET':
        if not publicaciones:
            print("Hola")
            contexto = {"publicaciones": None}
        else:
            print("Inagresa el else")
            contexto = {"publicaciones": publicaciones}
        return render(request, "index.html", contexto)
    else:
        print('Hola')
        print(request)
        if request.POST["Buscar"] != None:
            listaDeBusqueda =PublicacionInmobiliaria.objects.filter(titulo__in = request.POST["Buscar"])
            idPublicacion = PublicacionInmobiliaria.objects.get(titulo = request.POST["Buscar"]).id
            return publicacion(request,idPublicacion)
        else:
            print('Ingresa en el else del else')
            print(request)
            # PublicacionInmobiliaria.objects.filter(Q(numeroDormitorios = request.POST["numeroDormitorios"]) | Q(tipoInmueble = request.POST["tipoInmueble"]) | Q(tamaño = request.POST["tamaño"]) | Q(precio_range = [request.POST["minimo"], request.POST["maximo"]]))

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


def inmuebles(request):
    publicacionesInmuebles = PublicacionInmobiliaria.objects.all()
    print(publicacionesInmuebles)
    if request.method == 'GET':
        if not publicacionesInmuebles:
            return render(request, 'inmuebles.html',{'publicaciones': None})
        else:
            return render(request, 'inmuebles.html',{'publicaciones': publicacionesInmuebles})



