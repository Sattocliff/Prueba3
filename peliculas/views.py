from django.shortcuts import render
from .models import Pelicula, Genero, Director
# Create your views here.


def index(request):
    peliculas= Pelicula.objects.all()
    context={"peliculas":peliculas}
    return render(request, 'peliculas/index.html', context)

def crud(request):
    peliculas = Pelicula.objects.all()
    context = {'peliculas' : peliculas}
    return render(request, 'peliculas/peliculas_list.html', context)

def peliculasAdd(request):
    if request.method != 'POST':
        genero=Genero.objects.all()
        director=Director.objects.all()
        context={'genero':genero, 'director':director}
        return render(request,'peliculas/peliculas_add.html', context)
    else:
        nombrePelicula=request.POST["nombre_pelicula"]
        genero=request.POST["genero"]
        director=request.POST["director"]
        activo="1"
        objGenero=Genero.objects.get(id_genero = genero)
        objDirector=Director.objects.get(id_director = director)
        obj=Pelicula.objects.create(nombre_pelicula=nombrePelicula,
                            id_genero=objGenero,
                            id_director=objDirector,
                            activo=1)
        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render(request,'peliculas/peliculas_add.html', context)
    
def peliculas_del(request,pk):
    context={}
    try:
        pelicula=Pelicula.objects.get(nombre_pelicula=pk)
        pelicula.delete()
        mensaje="Bien, datos eliminados..."
        peliculas = Pelicula.objects.all()
        context={'peliculas': pelicula, 'mensaje': mensaje}
        return render(request, 'peliculas/peliculas_list.html', context)
        
        
    except:
        mensaje="Error, pelicula no existe..."
        peliculas= Pelicula.objects.all()
        context={'peliculas': peliculas, 'mensaje':mensaje}
        return render(request, 'peliculas/peliculas_list.html', context)
        