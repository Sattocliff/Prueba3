from django.db import models

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
    imagen = models.ImageField(upload_to="static/img", null=True)
    activo = models.IntegerField()
    
    def __str__(self):
        return str(self.nombre_pelicula)
    