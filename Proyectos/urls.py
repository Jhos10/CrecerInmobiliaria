from django.urls import path
from . import views
urlpatterns = [
 path('vistaProyectos/',views.proyectos, name='vistaPrincipalProyectos' ),
 path('<int:idProyecto>/proyecto', views.proyecto, name = 'proyecto') 
]