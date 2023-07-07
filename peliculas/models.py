from django.db import models
from django.db.models import Sum

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Director(models.Model):
    id_director = models.AutoField(db_column='idDirector', primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)

class Pelicula(models.Model):
    nombre_pelicula = models.CharField(primary_key=True, max_length=30)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    id_director = models.ForeignKey('Director',on_delete=models.CASCADE, db_column='idDirector')
    imagen = models.ImageField(upload_to="fotos", null=True)
    precio = models.IntegerField()
    activo = models.IntegerField()
    
    def __str__(self):
        return str(self.nombre_pelicula)
    

class Carro(models.Model):
    id_carro = models.AutoField(db_column='idCarro', primary_key=True)
    nombre_pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE, db_column='nombrePelicula')

    def precio_pelicula(self):
        return self.nombre_pelicula.precio
    
    @staticmethod
    def calcular_total():
        carros = Carro.objects.all()
        total = sum(carro.precio_pelicula() for carro in carros)
        return total




