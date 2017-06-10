from django.conf.urls import url
from django.contrib.auth import views as auth_views


from.import views


urlpatterns = [
        #url(r'^registrar/', views.registrar ),
        url(r'^$', views.index, name = 'index'),
        url(r'^home/$', views.home, name = 'home'),
        url(r'^profile/$', views.profile, name = 'profile'),
    #    url(r'^login/$', views.login, name = 'login'),
        url(r'^crear_usuario/$', views.crear_usuario, name = 'crear_usuario'),
        url(r'^login/$', auth_views.LoginView.as_view(template_name='Login.html' ,redirect_authenticated_user= True), name = 'login'),
        url(r'^logout/$', auth_views.LogoutView.as_view(template_name='Registro.html'), name = 'logout'),
        url(r'^upload/$', views.upload, name = 'upload'),


]
