from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name="index"),
    path('agregar-producto', agregarProducto,name="agregar-producto"),
    path('api', api,name="api"),
    path('carrito-vacio', carritoVacio,name="carrito-vacio"),
    path('carrito', carrito,name="carrito"),
    path('clima', clima,name="clima"),
    path('contacto', contacto,name="contacto"),
    path('inicio-sesion', inicioSesion,name="inicio-sesion"),
    
    path('metodo-de-pago', metodoDePago,name="metodo-de-pago"),
    path('planta1', planta1,name="planta1"),
    path('planta2', planta2,name="planta2"),
    path('registro', registro,name="registro"),
    path('seguimiento', seguimiento,name="seguimiento"),
    path('plantas', plantas,name="plantas"),
    path('form_planta', form_planta,name="form_planta"),
    path('form_mod_planta/<id>', form_mod_planta,name="form_mod_planta"),
    path('form_del_planta/<id>', form_del_planta,name="form_del_planta"),

]
