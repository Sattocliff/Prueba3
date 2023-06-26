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
    

def peliculas_findEdit(request,pk):

    if pk != "":
        pelicula = Pelicula.objects.get(nombre_pelicula=pk)
        genero = Genero.objects.all()
        director = Director.objects.all()

        print(type(pelicula.id_genero.genero))

        context={'pelicula':pelicula, 'genero':genero}
        if pelicula:
            return render(request, 'peliculas/peliculas_edit.html', context)
        else:
            context={'mensaje': "Error, esta pelicula no existe..."}
            return render(request, 'peliculas/peliculas_list.html', context)


def peliculasUpdate(request):
    if request.method == "POST":
        nombrePelicula=request.POST["nombre_pelicula"]
        genero=request.POST["genero"]
        director=request.POST["director"]
        activo="1"
        objGenero=Genero.objects.get(id_genero = genero)
        objDirector=Director.objects.get(id_director = director)

        pelicula = Pelicula()
        pelicula.nombre_pelicula=nombrePelicula
        pelicula.id_genero=objGenero
        pelicula.id_director=objDirector
        pelicula.activo=1
        pelicula.save()
        generos=Genero.objects.all()
        direc=Director.objects.all()
        context={'mensaje': "Ok, Datos actualizados...", 'generos':generos, 'direc':direc, 'pelicula': pelicula}
        return render(request, 'peliculas/peliculas_edit.html', context)
    else:
        peliculas = Pelicula.objects.all()
        context={'peliculas': peliculas}
        return render(request, 'peliculas/peliculas_list.html', context)