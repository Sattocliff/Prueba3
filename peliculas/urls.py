#from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns=[
    path('index', views.index, name='index'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('crud', views.crud, name='crud'),
    path('peliculasAdd', views.peliculasAdd, name='peliculasAdd'),
    path('peliculas_del/<str:pk>', views.peliculas_del, name='peliculas_del'),
    path('peliculas_findEdit/<str:pk>', views.peliculas_findEdit, name='peliculas_findEdit'),
    path('peliculasUpdate', views.peliculasUpdate, name='peliculasUpdate'),

    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),


]