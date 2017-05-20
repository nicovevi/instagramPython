from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'Registro.html')

def login(request):
    return render(request,'Log-in.html')

def home(request):
    return render(request,'home.html')

def crear_usuario(request):
    print(request.POST['email'])
    print(request.POST['name'])
    print(request.POST['username'])
    print(request.POST['password'])
    return render(request,'Log-in.html'
