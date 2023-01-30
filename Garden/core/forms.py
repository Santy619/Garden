
from django import forms
from .models import Planta

class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = [ 'idPlanta' , 'nombre', 'precio', 'stock', 'idCategoria' , 'imagen' ]

class UserForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = [ 'idPlanta' , 'nombre', 'precio', 'stock', 'idCategoria' , 'imagen' ]


