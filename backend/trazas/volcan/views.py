from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import VolcanModel
from .serializers import VolcanSerializer
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
from django.core import serializers
from mysql.connector import Error
import json


@api_view(['GET'])
def index(request):
    serializer_context = {
        'request': Request(request),
    }
    volcanes = VolcanModel.objects.all()
    serializer = VolcanSerializer(volcanes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def getNombreVolcanById(id):
    volcan = VolcanModel.objects.get(volcan_id=id)
    return volcan.nombre

@api_view(['POST'])
def create(request):
    serializer = VolcanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        volcanes = VolcanModel.objects.all()
        serializer = VolcanSerializer(volcanes, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def show(id):
    estacion = VolcanModel.objects.get(cod_event=id)
    return HttpResponse(estacion)


@api_view(["PUT"])
def update(request, id):
    try:
        volcanAux = VolcanModel.objects.get(volcan_id=id)
        serializer = VolcanSerializer(data=request.data, instance=volcanAux)
        if serializer.is_valid():
            serializer.save()
            volcanes = VolcanModel.objects.all()
            serializer = VolcanSerializer(volcanes, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def destroy(request, id):
    try:
        estacion = VolcanModel.objects.get(volcan_id=id)
        estacion.delete()
        volcanes = VolcanModel.objects.all()
        serializer = VolcanSerializer(volcanes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
from django.shortcuts import render

@api_view(['GET'])
def getAllEstacioneByVolcan(request):

    estacions = VolcanModel.objects.filter(volcan_id__isnull=False).values_list('nombre', 'altura')
    estacions.objects.create('nombre')
    #for estacion in estacions:
     #   estacion.nombre = 'jas'
    return Response(estacions, status=status.HTTP_200_OK)
