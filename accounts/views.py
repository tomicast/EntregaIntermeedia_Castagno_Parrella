from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required

from accounts.models import MasDatosUsuarioAvatar
from .forms import MyUserCreationForm, MyUserEditForm


def login(request):
    
    if request.method == 'POST':
        form= AuthenticationForm(request, data=request.POST)


        if form.is_valid():
            
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')   
                        
            user = authenticate(username= username, password= password)
            
            if user is not None:
                django_login(request, user)
                print ('pase por el login')
                redirect('inicio')
                
                return render(request, 'inicio.html', {})
            else:
                return render(request, 'accounts/login.html', {'form': form})
        else:
            return render(request, 'accounts/login.html', {'form': form})
                
                
    form= AuthenticationForm()
    return render (request, 'accounts/login.html', {'form': form})

def register(request):
    
    if request.method == 'POST':
        
        form = MyUserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html', {})
        else:
            return render(request, 'accounts/register.html', {'form': form})
    
    form= MyUserCreationForm()           
    
    return render (request, 'accounts/register.html', {'form': form})


@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')


@login_required
def editar_perfil(request):
    
    user = request.user
    mas_datos_usuario, _ = MasDatosUsuarioAvatar.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request. FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):    
                user.last_name = data.get('last_name')
                
            user.email = data.get('email') if data.get('email') else user.email
            user.mas_datos_usuario.avatar = data.get('avatar') if data.get('avatar') else mas_datos_usuario.avatar
            
            if data.get('password1') and data.get('password1') == data.get('password2'):
                user.set_password(data.get('password1'))
            
            user.mas_datos_usuario.save()
            user.save()                     
            
            return redirect('perfil') 
                    
        else:
            return render(request, 'accounts/editar_perfil.html', {'form': form})
    

    Form= MyUserEditForm(
        initial={
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'avatar': user.avatar
    }
    )
    return render(request, 'accounts/editar_perfil.html', {'form': form})