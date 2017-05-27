from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *
# Create your views here.
def index (request):
    return render(request,'Registro.html')

def login(request):
    return render(request,'Login.html')

def home(request):
    return render(request,'home.html')

def crear_usuario(request):

    user = User.objects.create_user (username = request.POST['username'], email = request.POST['email'], first_name = request.POST['name'], password = request.POST['password'])
    myuser = MiUsuario (usuario = user)
    print(user)
    print(user.password)
    return redirect ('login')
