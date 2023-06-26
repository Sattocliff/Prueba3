#from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns=[
    path('index', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('peliculasAdd', views.peliculasAdd, name='peliculasAdd'),
    path('peliculas_del/<str:pk>', views.peliculas_del, name='peliculas_del')


]