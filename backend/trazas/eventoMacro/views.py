from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EventoMacroModel
from .serializers import EventoMacroSerializer
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
    estaciones = EventoMacroModel.objects.all()
    print(estaciones)
    serializer = EventoMacroSerializer(estaciones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    serializer = EventoMacroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def show(request, id):
    evento = EventoMacroModel.objects.get(id_evento_macro=id)
    print(evento.volcan_id)
    serializer = EventoMacroSerializer(evento, many=True)
    return HttpResponse(serializer)

def validador(id):
    if(EventoMacroModel.objects.filter(id_evento_macro=id).exists()):
        return True
    else:
        return False

def createInternal(volcan_id, macro_evento, fecha_inicio, fecha_termino):
    eve = EventoMacroModel(id_evento_macro=macro_evento, volcan_id=volcan_id, inicio=fecha_inicio, fin=fecha_termino )
    eve.save()
    return True

@api_view(["PUT"])
def update(request, id):
    try:
        estacionAux = EventoMacroModel.objects.get(id_evento_macro=id)
        serializer = EventoMacroSerializer(data=request.data, instance=estacionAux)
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
        estacion = EventoMacroModel.objects.get(id_evento_macro=id)
        estacion.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
from django.shortcuts import render

# Create your views here.
