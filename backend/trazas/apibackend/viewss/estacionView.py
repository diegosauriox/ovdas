from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from ..models import EstacionModel
from ..serializers import EstacionSerializer
from rest_framework import viewsets

# Create your viewss here.
def index(request):
    localizados = EstacionModel.objects.all()
    return HttpResponse(localizados, content_type="application/json")

def create(request):
    serializer = EstacionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

def show(id):
    localizado = EstacionModel.objects.get(id=id)
    return  HttpResponse(localizado)

def update(request, id):
    estacion = EstacionModel.objects.get(id=id)
    serializer = EstacionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def destroy(id):
    estacion = EstacionModel.objects.get(id=id)
    estacion.delete()
    return index()