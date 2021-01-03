from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import IdentificacionSenalModel
from .serializers import IdentificacionSenalSerializer
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
    identificaciones = IdentificacionSenalModel.objects.all()
    print(identificaciones)
    serializer = IdentificacionSenalSerializer(identificaciones, context=serializer_context, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def filter(request):
    print(request.data.get('fechaIni'))
    identificaciones = IdentificacionSenalModel.objects.all().filter(est = request.data.get('estacion'))
    serializer = IdentificacionSenalSerializer(identificaciones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    serializer = IdentificacionSenalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def show(id):
    estacion = IdentificacionSenalModel.objects.get(cod_event=id)
    return HttpResponse(estacion)


@api_view(["PUT"])
def update(request, id):
    try:
        estacionAux = IdentificacionSenalModel.objects.get(cod_event=id)
        serializer = IdentificacionSenalSerializer(data=request.data, instance=estacionAux)
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
        estacion = IdentificacionSenalModel.objects.get(cod_event=id)
        estacion.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
from django.shortcuts import render

# Create your views here.
