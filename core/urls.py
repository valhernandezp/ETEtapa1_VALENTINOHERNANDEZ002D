from os import name
from django import urls
from django.urls import path
from .views import home,form_proveedor,Ver,form_mod_proveedor


urlpatterns = [
    path('',home,name="index"),
    path('form_proveedor',form_proveedor,name='form_proveedor'),
    path('ver',Ver,name="ver"),
    path('form_mod_proveedor/<id>',form_mod_pelicula,name="form_mod_proveedor")
]