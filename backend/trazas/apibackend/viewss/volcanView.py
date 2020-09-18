from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import VolcanModel
from ..serializers import VolcanSerializer
from django.core.exceptions import ObjectDoesNotExist
import json

# Create your viewss here.
@api_view(['GET'])
def getIdName(request):
    volcanes = VolcanModel.objects.all().values('id_volcan', 'nombre')

    return Response(volcanes, status=status.HTTP_200_OK)

@api_view(['GET'])
def index(request):
    volcanes = VolcanModel.objects.all()
    serializer = VolcanSerializer(volcanes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    serializer = VolcanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def show(id):
    volcan = VolcanModel.objects.get(id=id)
    return  HttpResponse(volcan)

@api_view(["PUT"])
def update(request, id):
    try:
        volcanAux = VolcanModel.objects.get(id_volcan=id)
        serializer = VolcanSerializer(data=request.data, instance =volcanAux)
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
        volcan = VolcanModel.objects.get(id_volcan=id)
        volcan.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)