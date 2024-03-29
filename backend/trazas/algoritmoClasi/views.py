from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AlgoritmoClasifiacionModel
from .serializers import Algoritmo_Clasi_Serializer
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
from django.core import serializers
from mysql.connector import Error
import json


# Create your viewss here.
@api_view(['GET'])
def index(request):
    serializer_context = {
        'request': Request(request),
    }
    estaciones = AlgoritmoClasifiacionModel.objects.all()
    print(estaciones)
    serializer = Algoritmo_Clasi_Serializer(estaciones, context=serializer_context, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    serializer = Algoritmo_Clasi_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return getAll()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getAll():
    algoritmos = AlgoritmoClasifiacionModel.objects.all()
    serializer = Algoritmo_Clasi_Serializer(algoritmos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def show(id):
    estacion = AlgoritmoClasifiacionModel.objects.get(id_algoritmo_clasi=id)
    return HttpResponse(estacion)


@api_view(["PUT"])
def update(request, id):
    try:
        estacionAux = AlgoritmoClasifiacionModel.objects.get(algoritmo_clasi_id=id)
        serializer = Algoritmo_Clasi_Serializer(data=request.data, instance=estacionAux)
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
        estacion = AlgoritmoClasifiacionModel.objects.get(algoritmo_clasi_id=id)
        estacion.delete()
        return getAll()
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
