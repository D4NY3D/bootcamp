from django.contrib import admin

# Register your models here.

from .models import Directores, Genre, Peliculas

admin.site.register(Directores)
admin.site.register(Genre)
admin.site.register(Peliculas)


