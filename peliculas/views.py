from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Pelicula, Genero, Director, Carro

from .forms import GeneroForm
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.shortcuts import redirect
# Create your views here.


def index(request):
    peliculas= Pelicula.objects.all()
    context={"peliculas":peliculas}
    queryset = request.GET.get("pelicula_buscada")

    if queryset:
        pelicula = Pelicula.objects.filter(
            Q(nombre_pelicula__icontains = queryset)
        ).first()
        request.session['id_pelicula'] = pelicula.nombre_pelicula
        return redirect(detalle_pelicula)
    
    return render(request, 'peliculas/index.html', context)

def contactanos(request):
    peliculas= Pelicula.objects.all()
    context={"peliculas":peliculas}
    return render(request, 'peliculas/contactanos.html', context)

def carrito(request):
    carritos= Carro.objects.all()
    context={"carritos":carritos}
    return render(request, 'peliculas/carrito.html', context)

def calcular(request):
    carritos = Carro.objects.all()
    total = Carro.calcular_total()
    return render(request, 'carrito.html', {'carritos': carritos, 'total': total})

def detalle_pelicula(request):
    pelicula = Pelicula.objects.filter(
        Q(nombre_pelicula__icontains = request.session['id_pelicula'])
    ).first()
    return render(request, 'peliculas/detalle_pelicula.html', {'pelicula': pelicula })

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
        descripcion=request.POST["descripcion"]
        precio=request.POST["precio"]
        imagen=request.FILES["imagen"]

        fs = FileSystemStorage()
        filename = fs.save(imagen.name, imagen)
        uploaded_file_url = fs.url(filename)

        activo="1"
        objGenero=Genero.objects.get(id_genero = genero)
        objDirector=Director.objects.get(id_director = director)
        obj=Pelicula.objects.create(nombre_pelicula=nombrePelicula,
                            id_genero=objGenero,
                            id_director=objDirector,
                            descripcion=descripcion,
                            imagen=uploaded_file_url,
                            precio=precio,
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

        context={'pelicula':pelicula, 'genero':genero, 'director':director}
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
        precio=request.POST["precio"]
        objGenero=Genero.objects.get(id_genero = genero)
        objDirector=Director.objects.get(id_director = director)
        imagen=request.POST["imagen"]

        pelicula = Pelicula()
        pelicula.nombre_pelicula=nombrePelicula
        pelicula.id_genero=objGenero
        pelicula.id_director=objDirector
        pelicula.precio=precio
        pelicula.imagen=imagen
        pelicula.activo=1
        pelicula.save()
        generos=Genero.objects.all()
        
        context={'mensaje': "Ok, Datos actualizados...", 'generos':generos, 'pelicula': pelicula}
        return render(request, 'peliculas/peliculas_edit.html', context)
    else:
        peliculas = Pelicula.objects.all()
        context={'peliculas': peliculas}
        return render(request, 'peliculas/peliculas_list.html', context)
    

def crud_generos(request):
    generos=Genero.objects.all()
    context={'generos':generos}
    print("enviando datos generos_list")
    return render(request,"peliculas/generos_list.html",context)


def generosAdd(request):
    print("Estoy en el controlador de generosAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = GeneroForm(request.POST)
        if form.is_valid:
            print("Es valido, voy a agregar")
            form.save()

            #limpiar form
            form=GeneroForm()

            context={'mensaje': "Ok, datos grabados...", "form":form}
            return render(request,"peliculas/generos_add.html", context)
    else:
        form = GeneroForm()
        context={'form':form}
        return render(request, 'peliculas/generos_add.html', context)
    


def generos_del(request,pk):
    mensajes=[]
    errores=[]
    generos = Genero.objects.all()
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("Bien, datos eliminados...")
            context={'generos': generos, 'mensajes':mensajes, 'errores': errores}
            return render(request,'peliculas/generos_list.html', context)
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        return render(request, 'peliculas/generos_list.html', context)
    


def generos_edit(request,pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("Edit encontró el genero...")
            if request.method == "POST":
                print("edit, es un POST")
                form= GeneroForm(request.POST,instance=genero)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context={'genero':genero, 'form': form, 'mensaje':mensaje}
                return render(request,'peliculas/generos_edit.html', context)
            else:
                #no es un post
                print("edit, no es un post")
                form = GeneroForm(instance=genero)
                mensaje=""
                context={'genero':genero,'form':form,'mensaje': mensaje}
                return render(request,'peliculas/generos_edit.html', context)
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'peliculas/generos_list.html', context)
    
