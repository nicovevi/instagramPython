from django.conf.urls import url



from . import views


urlpatterns = [
        #url(r'^registrar/', views.registrar ),
        url(r'^$', views.index, name = 'index'),
        url(r'^$', views.index, name = 'login'),


]
