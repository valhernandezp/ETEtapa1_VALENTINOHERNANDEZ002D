from django.shortcuts import redirect, render
from .models import Proveedor
from .forms import ProveedorForm
# Create your views here.

def home(request):
    proveedores= Provedor.objects.all()


    return render(request,'home.html',context={'datos':proveedores},
    
)

def form_proveedor(request):
    if request.method=='POST':
        proveedor_form=PeliculaForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('home')
    else:
        proveedor_form=ProveedorForm()
    return render(request,'core/form_crearproveedor.html',{'proveedor_form':proveedor_form})


def Ver(request):
    proveedores = Proveedor.objects.all()

    return render(request, 'core/ver.html', context={'proveedores':proveedores})


def form_mod_proveedor(request,id):
    proveedor = Proveedor.objects.get(titulo=id)

    datos ={
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST': 
        formulario = ProveedorForm(data=request.POST, instance = proveedor)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/form_mod_proveedor.html', datos)
