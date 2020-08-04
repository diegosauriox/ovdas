from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from ..models import EventoMacroModel
from ..serializers import EventoMacroSerializer
from rest_framework import viewsets

# Create your viewss here.
def index():
    evento = EventoMacroModel.objects.all()
    return HttpResponse(evento, content_type="application/json")

def create(request):
    serializer = EventoMacroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

def show(id):
    localizado = EventoMacroModel.objects.get(id=id)
    return  HttpResponse(localizado)

def update(request, id):
    localizado = EventoMacroModel.objects.get(id=id)
    serializer = EventoMacroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def destroy(id):
    localizado = EventoMacroModel.objects.get(id=id)
    localizado.delete()
    return index()