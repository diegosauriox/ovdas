from typing import re

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EstacionModel
from .serializers import EstacionSerializer
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
from django.core import serializers
from mysql.connector import Error
import json
from volcan.models import VolcanModel
from volcan.serializers import VolcanSerializer

# Create your viewss here.
@api_view(['GET'])
def index(request):
    serializer_context = {
        'request': Request(request),
    }
    estaciones = EstacionModel.objects.all()
    #estaciones = EstacionModel.objects.select_related('volcan')
    print(estaciones.query)
    serializer = EstacionSerializer(estaciones, many=True)

    #return Response(serializer.data, status=status.HTTP_200_OK)
    qs_json = serializers.serialize('json', estaciones)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def estacioneByVolcan(request, id):

    estacions = EstacionModel.objects.values('id_estacion', 'nombre').filter(volcan_id=id)
    # serializer = EstacionSerializer(estacions, many=True)
    # connection = mysql.connector.connect(host='localhost',
    #                                     database='ufro_ovdas',
    #                                     password='')

    # cursor = connection.cursor()
    # sql_fetch_blob_query = """SELECT estacion.*, volcan.nombre AS nombre_volcan from estacion INNER JOIN volcan
    #    ON estacion.volcan_id = volcan.id_volcan ORDER BY volcan.nombre DESC"""
    # cursor.execute(sql_fetch_blob_query)
    # record = cursor.fetchall()
    return Response(estacions, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    vol = VolcanModel.objects.get(volcan_id=request.data['volcan_id'])
    serializer = EstacionSerializer(data=request.data)
    if serializer.is_valid():
        #print(serializer.data)
        serializer.save(volcan=vol)
        return getAll()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getAll():
    estaciones = EstacionModel.objects.all()
    serializer = EstacionSerializer(estaciones, many=True)
    return serializer.data

@api_view(['GET'])
def show(request):
    estacion = EstacionModel.objects.filter(volcan_id=id)
    return  HttpResponse(estacion)
def estacioneByVolcan(id):
    estaciones = EstacionModel.objects.values('estacion_id', 'nombre','latitud','longitud').filter(volcan_id=id)
    return estaciones
    
@api_view(["PUT"])
def update(request, id):
    try:
        estacionAux = EstacionModel.objects.get(estacion_id=id)
        serializer = EstacionSerializer(data=request.data, instance =estacionAux)
        if serializer.is_valid():
            serializer.save()
            return getAll()
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def destroy(request, id):
    try:
        estacion = EstacionModel.objects.get(estacion_id=id)
        estacion.delete()
        return getAll()
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)

