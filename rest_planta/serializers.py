from dataclasses import fields
from rest_framework import serializers
from core.models import *

class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields =[ 'idPlanta' , 'nombre', 'precio', 'stock', 'idCategoria' , 'imagen' ]