from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import FormLibro, busquedaLibro
from datetime import datetime
from django.contrib.auth.decorators import login_required

from .models import Libro


def inicio(request):
    return render(request, 'inicio.html')


def listado_libros(request):
    
    nombre_de_busqueda=request.GET.get("titulo")
    
    if nombre_de_busqueda:
        listado_libros= Libro.objects.filter(titulo__icontains=nombre_de_busqueda) 
         
    else:   
        listado_libros= Libro.objects.all()
    
    form=busquedaLibro()
    return render (request,"libro/listado_libros.html", {"listado_libros":listado_libros,"form":form })


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
                anio=data.get('anio') if data.get('anio') else datetime.now()                
            )
            libro.save()

            return redirect('listado_libros')
        
        else:
            return render(request, 'libro/crear_libro.html', {'form': form})
              
    form_libro = FormLibro()
    
    return render(request, 'libro/crear_libro.html', {'form': form_libro})


def about(request): 
    
    return HttpResponse ("En esta página es posible ver el listado de todos los libros. Además se podrá cargar nuevos libros y buscar libros")


@login_required
def eliminar_libro(request, id): 
    libro = Libro.objects.get(id=id)
    libro.delete()
    
    return redirect('listado_libros')


@login_required
def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormLibro(request.POST)
        
        if form.is_valid():
            libro.titulo = form.cleaned_data.get('titulo')
            libro.editorial = form.cleaned_data.get('editorial')
            libro.anio = form.cleaned_data.get('fecha_de_publicación')
            libro.save()
            
            return redirect('listado_libros') 
                    
        else:
            return render(request, 'libro/editar_libro.html', {'form': form, 'libro': libro})
    
    form_libro = FormLibro(initial= {'titulo': libro.titulo , 'editorial': libro.editorial, 'anio': libro.anio})
        
    return render(request, 'libro/editar_libro.html', {'form': form_libro, 'libro': libro})


def mostrar_libro(request, id):
    libro = Libro.objects.get(id=id)
    return render(request,'libro/mostrar_libro.html', {'libro': libro})