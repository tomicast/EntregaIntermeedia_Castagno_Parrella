from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Comic


class ListadoComics(ListView):
    model= Comic
    template_name = 'comic/listado_comics.html'

    
    
class CrearComic(CreateView):
    model= Comic 
    template_name = 'comic/crear_comic.html' 
    success_url = '/appcomic/comics'
    fields = ['titulo', 'editorial', 'anio']
          
          
class EditarComic(LoginRequiredMixin, UpdateView): 
    model= Comic 
    template_name = 'comic/editar_comic.html'
    success_url = '/appcomic/comics'
    fields = ['titulo', 'editorial', 'anio']

            
class EliminarComic(LoginRequiredMixin, DeleteView): 
    model= Comic 
    template_name = 'comic/eliminar_comic.html' 
    success_url = '/appcomic/comics'
 
      
class MostrarComic(DetailView):
    model= Comic 
    template_name = 'comic/mostrar_comic.html' 
