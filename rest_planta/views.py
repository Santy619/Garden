from ast import If
from urllib import request
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Planta
from .serializers import PlantaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET' , 'POST'])
@permission_classes((IsAuthenticated,))
def lista_plantas(request):

    # Lista todas la Plantas

    if request.method == 'GET':
        planta = Planta.objects.all()
        serializer = PlantaSerializer(planta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlantaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REUQUEST)

@api_view(['GET' , 'PUT', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def detalle_planta(request,id):

    # GET,UPDATE O DELETE DE UNA PLANTA

    try:
        planta = Planta.objects.get(idPlanta=id)
    except Planta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PlantaSerializer(planta)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PlantaSerializer(planta, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.http_404_BAD_REQUEST)
    elif request.method == 'DELETE':
        planta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
