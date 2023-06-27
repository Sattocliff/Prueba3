from django.contrib import admin
from .models import Genero, Director, Pelicula,Carro
# Register your models here.


admin.site.register(Genero)
admin.site.register(Director)
admin.site.register(Pelicula)
admin.site.register(Carro)