from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EstacionModel
from .serializers import EstacionSerializer
from django.core.exceptions import ObjectDoesNotExist
import json

# Create your viewss here.
@api_view(['GET'])
def index(request):
    estaciones = EstacionModel.objects.all()
    serializer = EstacionSerializer(estaciones, many=True )
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    serializer = EstacionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def show(id):
    estacion = EstacionModel.objects.get(id=id)
    return  HttpResponse(estacion)

@api_view(["PUT"])
def update(request, id):
    try:
        estacionAux = EstacionModel.objects.get(id_estacion=id)
        serializer = EstacionSerializer(data=request.data, instance =estacionAux)
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
        estacion = EstacionModel.objects.get(id_estacion=id)
        estacion.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)