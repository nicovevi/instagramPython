from django.conf.urls import url



from . import views


urlpatterns = [
        #url(r'^registrar/', views.registrar ),
        url(r'^$', views.index, name = 'index'),
        url(r'^login/$', views.login, name = 'login'),
        url(r'^home/$', views.home, name = 'home'),
        url(r'^crear_usuario/$', views.crear_usuario, name = 'crear_usuario'),



]
