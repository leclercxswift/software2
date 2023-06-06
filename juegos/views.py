from django.shortcuts import render,redirect, get_object_or_404
from .forms import UserRegisterForm, PublicacionesForm
from django.contrib.messages import constants as messages_constants
from django.contrib.messages import constants as messages
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def inicio(request):
    return render(request,'home.html')
def registro(request):
    registered = False  # Variable para indicar si el registro fue exitoso

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            registered = True  # Establecer como True si el registro fue exitoso

    else:
        form = UserRegisterForm()

    context = {'form': form, 'registered': registered}
    return render(request, 'registro.html', context)
def login(request):
    return render(request,'login.html')
def logout_view(request):
    messages.success(request, "¡Has cerrado sesión exitosamente!")
    logout(request)
    return redirect('inicio')
def contacto(request):
    return render(request,'contacto.html')

@login_required(login_url='login')
def comunidad(request):
    publicaciones= Publicaciones.objects.all()
    context={'publicaciones':publicaciones}
    return render(request, 'comunidad.html', context)
def publicar(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    
    if request.method == 'POST':
        form = PublicacionesForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, '¡Publicado!')
            return redirect('comunidad')
        else:
            messages.error(request, 'Error al publicar')
    
    form = PublicacionesForm()
    return render(request, 'publicar.html', {'form': form})
def perfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        publicaciones = user.publicaciones.all()
    else:
        publicaciones = current_user.publicaciones.all()
        user = current_user
    return render(request, 'perfil.html', {'user': user, 'publicaciones': publicaciones})

def follow(request,username):

    current_user= request.user
    to_user= User.objects.get(username=username)
    to_user_id= to_user
    rel=Relationship(from_user=current_user,to_user=to_user_id)
    rel.save()
    messages.success(request, f'sigues a {username}')
    return redirect('comunidad')

def unfollow(request,username):

    current_user= request.user
    to_user= User.objects.get(username=username)
    to_user_id= to_user
    rel=Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'ya no sigues a {username}')
    return redirect('comunidad')

