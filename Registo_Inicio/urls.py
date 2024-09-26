from django.urls import path
from . import views

urlpatterns = [
    path("Registro/", views.registroUsuario, name="registro"),
    path("inicioSesion/", views.inicioSesionUsuario, name ="inicioSesion"),
    path("perfilUsuario/", views.perfilUsuario, name = "perfilUsuario")
]