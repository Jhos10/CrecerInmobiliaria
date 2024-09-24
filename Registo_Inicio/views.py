from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def registroUsuario(request):
    if request.method == "GET":
        return render(request,"registro.html")
    else:
        if request.POST["password"] == request.POST["passwordDos"]:
            usuario = User.objects.create_user(username=request.POST["username"],email= request.POST["email"], password= request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
            usuario.save()
            print("Usuario creado con exito")
            return HttpResponse("Usuario creado con exito")
        else:
            print("El usuario no fue creado con exito")
            return HttpResponse("El usuario no pudo ser creado")