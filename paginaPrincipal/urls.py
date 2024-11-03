from django.urls import path
from . import views

urlpatterns = [
  path('', views.paginaPrincipal, name = "paginaPrincipal"),
  path('<int:idPublicacion>/publicacion', views.publicacion, name = 'publicacion'),
  path('inmuebles/', views.inmuebles, name='inmuebles')
]

