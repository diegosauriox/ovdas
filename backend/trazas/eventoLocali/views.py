
from datetime import date, datetime, timedelta
from MySQLdb import Date
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from eventoMacro.views import getClasificacion, getEventoMacroId
from alertas.serializers import AlertasSerializer2
from .models import EventoLocalizadoModel
from .serializers import EventoLocaliSerializer, EventoLocaliSerializer2, EventoLocaliSerializer3
from alertas.models import AlertasModel
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
from django.core import serializers
from mysql.connector import Error
import json
import numpy as np

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

@api_view(['GET'])
def getLocalizacionByAlertas(request):
    alertas = AlertasModel.objects.all()
    serializer= AlertasSerializer2(alertas, many=True)
    localizadosByAlertas=[]
    for alerta in serializer.data:
        localizado=EventoLocalizadoModel.objects.filter(evento_macro_id=alerta["evento_id"]).first()
        localizadosByAlertas.append(localizado)
    reverse=np.flip(localizadosByAlertas)
    localizacionSerializer=EventoLocaliSerializer(reverse,many=True)

    return Response(reverse,status=status.HTTP_200_OK)


@api_view(['GET'])
def getLocalibyId(request,id):
    
    #localizaciones = EventoLocalizadoModel.objects.all()
    localizaciones=EventoLocalizadoModel.objects.filter(evento_macro=id)
    
    serializer = EventoLocaliSerializer(localizaciones, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def dataToPdf(request):
    serializer_context = {
        'request': Request(request),
    }
    #localizaciones = EventoLocalizadoModel.objects.all()
    localizaciones=EventoLocalizadoModel.objects.values("evento_macro_id","tiempo","ml","lat","lon","z")
    print(localizaciones) 
    #serializer = EventoLocaliSerializer(localizaciones, context=serializer_context, many=True)
    return Response(localizaciones, status=status.HTTP_200_OK)



def getMlById(id):
    print(id)
    print('esta buscando ml por id')
    localizado =EventoLocalizadoModel.objects.filter(evento_macro_id=id).first()
    print(localizado)
    return localizado.ml

def getAllLocalizadoByMl():
    localizacionesMl=EventoLocalizadoModel.objects.filter(tiempo__range=('2017-11-16 00:00:00',"2018-08-23 00:00:00"))
    #serializer=EventoLocaliSerializer(localizacionesMl,many=True)
    return localizacionesMl


@api_view(['POST'])
def getLocalizacionesBytiempo(request):
    print(request.data)
    #localizaciones = EventoLocalizadoModel.objects.all()
    localizaciones=EventoLocalizadoModel.objects.filter(tiempo__range=(request.data["fechaIni"],request.data["fechaFin"]))
    print(localizaciones) 
    serializer = EventoLocaliSerializer(localizaciones,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def getAllCountLocalizado():
    fechaActual=datetime.now()
    fecha1=fechaActual.strftime("%Y-%m-%d %H:%M:%S")
    fecha2=(fechaActual-timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
    localizaciones30Min=EventoLocalizadoModel.objects.filter(tiempo__range=('2017-11-16 00:00:00',"2017-12-16 00:00:00"))
    serializer=EventoLocaliSerializer(localizaciones30Min,many=True)
    contador=0
    for localizacion in serializer.data:
        if(getEventoMacroId(localizacion["evento_macro_id"]).clasificacion=="VT"):
            contador=contador+1
    return contador, serializer.data[0]["evento_macro_id"]

    #return localizacionesMl
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
    localizaciones = EventoLocalizadoModel.objects.values_list('evento_macro_id','evento_loc_id', 'ml','z')[:5]
    
    #print(localizaciones[0][0])
    """ data=list(localizaciones)
    for localizacion in data:
        localizacion=list(localizacion)    
        print(getClasificacion(localizacion[0]))
        localizacion.insert(0,getClasificacion(localizacion[0]))
     """
    serializer = EventoLocaliSerializer2(localizaciones, context=serializer_context, many=True)
    return Response(localizaciones, status=status.HTTP_200_OK)
