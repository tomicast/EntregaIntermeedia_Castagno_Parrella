from django.urls import path
from .views import login, register 
from django.contrib.auth.views import LogoutView

#modelo
# path('url', vista, nombre=x)

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('register/', register, name= 'register'),
    ]  