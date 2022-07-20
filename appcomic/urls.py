from django.urls import path
from . import views


urlpatterns = [
    path('comics/', views.ListadoComics.as_view(), name='listado_comics'),
    path('crear-comic/', views.CrearComic.as_view(), name='crear_comic'),
    path('editar-comic/<int:pk>/', views.EditarComic.as_view(), name='editar_comic'),
    path('eliminar-comic/<int:pk>/' , views.EliminarComic.as_view(), name='eliminar_comic'),
    path('mostrar-comic/<int:pk>', views.MostrarComic.as_view() , name='mostrar_comic'),
    ]

    
