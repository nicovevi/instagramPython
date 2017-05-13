from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'Registro.html')

def login(request):
    return render(request,'Log-in.html')

def home(request):
    return render(request,'home.html')
