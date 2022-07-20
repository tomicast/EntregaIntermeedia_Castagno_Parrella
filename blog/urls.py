from django.urls import path
from .views import inicio, listado_libros, crear_libro, about, eliminar_libro, editar_libro, mostrar_libro


urlpatterns = [
    path('', inicio, name='inicio'),
    path('listado-libros/', listado_libros, name='listado_libros'),
    path('crear-libro/', crear_libro, name='crear_libro'),
    path ("about/", about, name="about" ),
    path('editar-libro/<int:id>', editar_libro, name='editar_libro'),
    path('eliminar-libro/<int:id>', eliminar_libro, name='eliminar_libro'),
    path('mostrar-libro/<int:id>', mostrar_libro, name='mostrar_libro'),
    ]

    
 