from django.contrib import admin
# from django.contrib.auth.models import User
from . import models

# Registrar el apartado publicacion de inmobiliaria en el admin
admin.site.register(models.PublicacionInmobiliaria)
admin.site.register(models.ImagenPublicacion)
admin.site.register(models.User_PublicacionInmobiliaria)
