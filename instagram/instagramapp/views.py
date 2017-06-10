from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage  import FileSystemStorage
# Create your views here.
def index (request):
    return render(request,'Registro.html')

def upload (request):
    return render(request,'upload.html')

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

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def uploadfile (request):
    curr_user = request.user;
    post_user = Post.objects.filter(creador=curr_user),count();
    mediaFile = request.FILES['photo'];
    newNameFile = curr_user.username + "-" + str(curr_user.id) + "-" + str(post_user)
    fs = FileSystemStorage()
    filename = fs.save(newNameFile, mediaFile)
    uploaded_file_url = url(filename)
    photo = uploaded_file_url;
    description = request.POST [ 'description'];
    newPost = Post ( foto = photo, descripcion = description, user_id = curr_user );
    newPost = save();
    media_user = Post.objects.filter( creador = curr_user.id );
    context = {'curr_user': curr_user, 'media_user': media_user}
    return render (request, 'instagram/profile.html', context)
