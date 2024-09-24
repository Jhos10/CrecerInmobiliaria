from django.urls import path
from . import views

urlpatterns = [
    path("Registro/", views.registroUsuario, name="Registro")
]