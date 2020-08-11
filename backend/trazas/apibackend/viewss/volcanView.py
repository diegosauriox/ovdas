from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import VolcanModel
from ..serializers import VolcanSerializer

# Create your viewss here.
@api_view(['GET'])
def index(request):
    volcanes = VolcanModel.objects.all()
    serializer = VolcanSerializer(volcanes, many=True )
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

def update(request, id):
    volcan = VolcanModel.objects.get(id=id)
    serializer = VolcanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def destroy(id):
    volcan = VolcanModel.objects.get(id=id)
    volcan.delete()
    return index()