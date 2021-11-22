from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from numpy import array
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AlertasModel
from django.core import serializers
from .serializers import AlertasSerializer
""" from .serializers import EventoMacroSerializer
 """
from eventoMacro.views import getEstacionesByEventoMacroById as getEstacionesByEventoMacroById
from volcan.views import getNombreVolcanById as getNombreVolcanById
from eventoLocali.views import getMlById as getMlById
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
from django.core import serializers
from mysql.connector import Error
import json

@api_view(['GET'])
def obtenerAlertas(request):
    #alertas = AlertasModel.objects.all()
    alertas = AlertasModel.objects.select_related('evento')
    #print(alertas.query)
    #alertas = AlertasModel.filter(eventob__isnull=False)
    #serializer = AlertasSerializer(alertas, many=True)
    datosAlerta=[]
    for alerta in alertas:
        #print(alerta.evento_id)
        datos=getEstacionesByEventoMacroById(alerta.evento_id)
        #print(datos["clasificacion"])
        clasificacion=datos["clasificacion"]
        volcan_id=datos["volcanid"]
        nombreVolcan=getNombreVolcanById(volcan_id)
        #print(nombreVolcan.) 
        ml=getMlById(alerta.evento_id)
        #print(ml)
        json={"volcan":nombreVolcan,"ml":ml,"clasificacion":clasificacion,"tiempo":alerta.created_at}
        datosAlerta.append({"volcan":nombreVolcan,"ml":ml,"clasificacion":clasificacion,"tiempo":alerta.created_at}) 
        print (datosAlerta)
        #print(json)
    #return HttpResponse(alertas, status=status.HTTP_200_OK)
    
    qs_json = serializers.serialize('json', alertas)
    
    return Response(datosAlerta,status=status.HTTP_200_OK)
# Create your views here.

