from django.urls import path
from .views import login, register, perfil, editar_perfil
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', register, name= 'register'),
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil')
    ]  