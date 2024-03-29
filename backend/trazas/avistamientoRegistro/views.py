from decimal import Context
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from .models import AvistamientoRegistroModel
from .serializers import AvistamientoRegistroSerializer
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
from django.core import serializers
from mysql.connector import Error
import json
from eventoMacro.models import EventoMacroModel

# Create your viewss here.


@api_view(['GET'])
def PSCoda(request,id):
    serializer_context = {
        'request': Request(request),
    }
    print(id)
    avistamiento=AvistamientoRegistroModel.objects.filter(evento_macro_id=id)
    
    serializer = AvistamientoRegistroSerializer(avistamiento, context=serializer_context,many=True)
    print("tiempo coda"+serializer.data[0]["coda"])

    datos=[]
    datos.append(serializer.data[0]["t_p"])
    datos.append(serializer.data[0]["t_s"])
    datos.append(serializer.data[0]["coda"])
    
    return Response(datos, status=status.HTTP_200_OK)

def getAvistamientoByMacroId(id):
    avistamiento=AvistamientoRegistroModel.objects.filter(evento_macro_id=id)
    serializer = AvistamientoRegistroSerializer(avistamiento,many=True)
    return serializer.data

@api_view(['GET'])
def index(request):
    serializer_context = {
        'request': Request(request),
    }
    estaciones = AvistamientoRegistroModel.objects.all()
    print(estaciones)
    serializer = AvistamientoRegistroSerializer(estaciones, context=serializer_context, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    serializer = AvistamientoRegistroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def show(id):
    estacion = AvistamientoRegistroModel.objects.get(cod_event=id)
    return HttpResponse(estacion)


@api_view(["PUT"])
def update(request, id):
    try:
        estacionAux = AvistamientoRegistroModel.objects.get(cod_event=id)
        serializer = AvistamientoRegistroSerializer(data=request.data, instance=estacionAux)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def destroy(request, id):
    try:
        estacion = AvistamientoRegistroModel.objects.get(cod_event=id)
        estacion.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)

