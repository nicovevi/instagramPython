from django.conf.urls import url



from . import views


urlpatterns = [
        #url(r'^registrar/', views.registrar ),
        url(r'^$', views.index, name = 'index'),
        url(r'^login/$', views.index, name = 'login'),
        url(r'^home/$', views.index, name = 'home'),
        url(r'^crear_usuario/$', views.crear_usuario, name = 'crear_usuario'),



]
