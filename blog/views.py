from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import FormLibro, busquedaLibro
from .models import Libro
from datetime import datetime


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def listado_libros(request):
    nombre_de_busqueda=request.GET.get("nombre")
    
    if nombre_de_busqueda:
        listado_libros= Libro.objects.filter(nombre__icontains=nombre_de_busqueda)  
    else:   
        listado_libros= Libro.objects.all()
    
    form=busquedaLibro()
    return render (request,"listado_libros.html", {"listado_libros":listado_libros,"form":form })

def crear_libro(request):
    if request.method == 'POST':
        form = FormLibro(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('anio')
            if not fecha:
                fecha = datetime.now() 
            
            libro = Libro(
                titulo=data.get('titulo'),
                editorial=data.get('editorial'),
                anio=fecha
                
            )
            libro.save()


            return redirect('listado_libros')
        
        else:
            return render(request, 'crear_libro.html', {'form': form})
            
    
    form_libro = FormLibro()
    
    return render(request, 'crear_libro.html', {'form': form_libro})

def about(request):
    
    return HttpResponse ("En esta página es posible ver el listado de todos los libros. Además se podrá cargar nuevos libros y buscar libros")

# def listado_perros(request):
    
#     nombre_de_busqueda = request.GET.get('nombre')
    
#     if nombre_de_busqueda:
#         listado_perros = Perro.objects.filter(nombre__icontains=nombre_de_busqueda) 
#     else:
#         listado_perros = Perro.objects.all()
    
#     form = BusquedaPerro()
#     return render(request, 'listado_perros.html', {'listado_perros': listado_perros, 'form': form})
    