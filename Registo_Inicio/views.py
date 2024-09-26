from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
# from django.db import connection
# from .models import PublicacionInmobiliaria
from django.db.models import Q
# Create your views here.
# Vista para registrar el usuario
def registroUsuario(request):
    # Condicional para saber con que metodo esta interactuando el usuario
    if request.method == "GET":
        # Carga el html si el usuario ingresa atraves del metodo get
        return render(request,"registro.html")
    else:
        # Mira si la contraseña concuerda con la contraseña dos(Contraseña Confirmacion)

        # Si coincide es porque se puede crear el usuario
        if request.POST["password"] == request.POST["passwordDos"]:
         
            # Se crear un queryset con los datos que coincidan con los datos enviados por el usuario atraves del metodo post
            usuarios = User.objects.filter(Q( username = request.POST["username"]) | Q(email = request.POST["email"]))

            # Si hay usuarios con los mismos datos que el usuario ingreso
            if usuarios.exists():

                print(usuarios)
                # Le genera un html con el siguiente mensaje
                return redirect("inicioSesion")
            # Si no existe ninguno se crea un nuevo usuario
            else:
                
                # Se crea un nuevo usuario
                nuevoUsuario = User.objects.create_user(username= request.POST["username"], 
                email = request.POST["email"], password = request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
                #
                print(usuarios)
                # Se muestra el html con un mensaje de usuario creado con exito
                return HttpResponse("Usuario creado con exito")

        else:
            # 
            print("El usuario no fue creado con exito")
            return HttpResponse("El usuario no pudo ser creado")
        
# @csrf_protect
@never_cache
def inicioSesionUsuario(request):
    # pass
    if request.method == "GET":
        return render(request, 'inicioSesion.html')
    else:
        usuario = authenticate(username=request.POST["username"], password=request.POST["password"])

        if usuario != None:
            login(request, usuario)
            print("El usuario se encuentra en la base de datos")
            return redirect('perfilUsuario')
        
        else:
            print("Usuario no esta en la base de datos")
            return redirect('registro')
            # login()

def perfilUsuario(request):
    usuario = request.user
    return render(request, 'perfil.html', {
        'usuario': usuario
    })