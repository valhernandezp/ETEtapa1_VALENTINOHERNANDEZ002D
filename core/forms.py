from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.db.models import fields
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria,Proveedor




class PeliculaForm(ModelForm):

    class Meta:
        model=Pelicula
        fields=['idProveedor','Nombre','Telefono','Direccion','Email','Pais','Contraseña','Moneda']
        labels ={
            'idProveedor':'Ingrese el Id del proveedor',
            'Nombre':'Ingrese el protagonista de la pelicula',
            'Telefono':'Ingrese la sinopsis de la pelicula',
            'genero':'seleccione el genero de la pelicula'
        }
        widgets= {
            'idProveedor':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Id del proveedor',
                    'id':'IdProveedor'
                }
            ),

            'Nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre del proveedor',
                    'id':'Nombre'
                }
            ),

            'Telefono':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Telefono del proveedor',
                    'id':'Telefono'
                }
            ),

            'Direccion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Direccion del proveedor',
                    'id':'Direccion'
                }
            ),

            'Email':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Email del proveedor',
                    'id':'Email'
                }
            ),

            'Pais':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Pais del proveedor',
                    'id':'Pais'
                }
            ),

            'Contraseña':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Contraseña del proveedor',
                    'id':'Contraseña'
                }
            ),

            'Moneda':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Tipo de moneda (dolar o pesos chilenos)',
                    'id':'Moneda'
                }    
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Categoria',
                    'id':'categoria'
                }
            )


        }