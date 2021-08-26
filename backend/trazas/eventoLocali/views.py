from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EventoLocalizadoModel
from .serializers import EventoLocaliSerializer, EventoLocaliSerializer2
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
    localizaciones = EventoLocalizadoModel.objects.all()
    print(localizaciones)
    serializer = EventoLocaliSerializer(localizaciones, context=serializer_context, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    serializer = EventoLocaliSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def show(id):
    estacion = EventoLocalizadoModel.objects.get(id_evento_loc=id)
    return HttpResponse(estacion)


@api_view(["PUT"])
def update(request, id):
    try:
        estacionAux = EventoLocalizadoModel.objects.get(id_evento_loc=id)
        serializer = EventoLocaliSerializer(data=request.data, instance=estacionAux)
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
        estacion = EventoLocalizadoModel.objects.get(id_evento_loc=id)
        estacion.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def loadLastItem(request):
    serializer_context = {
        'request': Request(request),
    }
    #localizaciones = EventoLocalizadoModel.objects.filter(ml__gte = 2).order_by('evento_loc_id')[:5]
    localizaciones = EventoLocalizadoModel.objects.values_list('evento_loc_id', 'ml')
    print(localizaciones)
    serializer = EventoLocaliSerializer2(localizaciones, context=serializer_context, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
