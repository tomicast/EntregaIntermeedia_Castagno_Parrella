
from django.urls import path
from .views import inicio, listado_libros, crear_libro, about

#modelo
# path('url', vista, nombre=x)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('listado-libros/', listado_libros, name='listado_libros'),
    path('crear-libro/', crear_libro, name='crear_libro'),
    path ("about/", about ),
    ]

    
    # path('base/', base   ),