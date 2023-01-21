from tkinter import image_names
from django.shortcuts import render,redirect
from django import forms
from .views import *
from .forms import PlantaForm
from .models import Planta
# from .forms import PlantaForm




# Create your views here.
def index(request):
    return render(request, 'core/index.html',)
    

def agregarProducto(request):
    return render(request, 'core/agregar-producto.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def api(request):
    return render(request, 'core/api.html')

def carritoVacio(request):
    return render(request, 'core/carrito-vacio.html')

def clima(request):
    return render(request, 'core/clima.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def inicioSesion(request):
    return render(request, 'core/inicio-sesion.html')

def metodoDePago(request):
    return render(request, 'core/metodo-de-pago.html')

def planta1(request):
    return render(request, 'core/planta1.html')

def planta2(request):
    return render(request, 'core/planta2.html')

def registro(request):
    return render(request, 'core/registro.html')

def seguimiento(request):
    return render(request, 'core/seguimiento.html')

def plantas(request):

    plantas = Planta.objects.all()

    datos={
        'plantas' : plantas
    }
    return render(request, 'core/plantas.html', datos)

def form_planta(request):
     
    datos = {
        'form' : PlantaForm()
    }

    if request.method == 'POST':

        formulario = PlantaForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    
    return render(request, 'core/form_planta.html',datos)

    
def form_mod_planta(request,id):

    planta = Planta.objects.get(idPlanta=id)

    datos = {
        'form' : PlantaForm(instance=planta)
    }

    if request.method == 'POST':
        formulario = PlantaForm(request.POST, instance=planta)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form_mod_planta.html', datos)

def form_del_planta(request, id):

    planta = Planta.objects.get(idPlanta=id)

    planta.delete()

    return redirect(to="plantas")