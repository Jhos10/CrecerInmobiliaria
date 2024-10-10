from django.urls import path
from . import views

urlpatterns = [
 path('SobreNosotros/', views.inmobiliaria_view, name = 'sobreNosotros')
]