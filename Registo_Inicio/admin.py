from django.contrib import admin
# from django.contrib.auth.models import User
from .models import PublicacionInmobiliaria

# Registrar el apartado publicacion de inmobiliaria en el admin
admin.site.register(PublicacionInmobiliaria)

