from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def index (request):
    return render(request,'Registro.html')

def login(request):
    return render(request,'Login.html')

@login_required
def home(request):
    return render(request,'home.html')

def crear_usuario(request):

    user = User.objects.create_user (username = request.POST['username'], email = request.POST['email'], first_name = request.POST['name'], password = request.POST['password'])
    myuser = MiUsuario (usuario = user)
    print(user)
    print(user.password)
    return redirect ('login')

def profile(request):
    return render(request,'profile.html')
