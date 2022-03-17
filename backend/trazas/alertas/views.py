from itertools import count
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from numpy import array
import numpy as np
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AlertasModel
from django.core import serializers
from .serializers import AlertasSerializer, AlertasSerializer2
""" from .serializers import EventoMacroSerializer
 """
from eventoMacro.views import getEstacionesByEventoMacroById as getEstacionesByEventoMacroById
from volcan.views import getNombreVolcanById as getNombreVolcanById
from eventoLocali.views import getMlById as getMlById
from eventoLocali.views import getAllLocalizadoByMl as getAllLocalizadoByMl
from eventoLocali.views import getAllCountLocalizado as getAllCountLocalizado
from eventoMacro.views import getEventoMacroId as getEventoMacroId
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
from django.core import serializers
from mysql.connector import Error
import json
from datetime import date

from background_task import background


@api_view(['GET'])
def obtenerAlertas(request):
    alertas = AlertasModel.objects.all()
    print("hola")
    
    datosAlerta=[]
    for alerta in alertas:
        print(alerta.evento_id) 
        datos=getEstacionesByEventoMacroById(alerta.evento_id)     
        clasificacion=datos["clasificacion"]
        print(clasificacion)
        volcan_id=datos["volcanid"]
        nombreVolcan=getNombreVolcanById(volcan_id) 
        ml=getMlById(alerta.evento_id)
        datosAlerta.append({"volcan":nombreVolcan,"ml":ml,"clasificacion":clasificacion,"motivo":alerta.motivo,"tiempo":alerta.created_at}) 
        print (datosAlerta)
    reverse=np.flip(datosAlerta)
    return Response(reverse,status=status.HTTP_200_OK)

@api_view(["GET"])
def getAllAlertas(request):
    alertas = AlertasModel.objects.all()
    serializer= AlertasSerializer2(alertas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def guardarAlertas(request):

    #eventoLocalizado=getAllLocalizadoByMl()[:10000]

    eventoLocalizado=getAllLocalizadoByMl()
    bla=[]
    for evento in eventoLocalizado:
        bla.append(evento.ml)
        if(evento.ml>1):
            eventoMacro=getEventoMacroId(evento.evento_macro_id)  
            alerta= AlertasModel(evento=eventoMacro,motivo="Cantidad Ml sobre el criterio")
            alerta.save()
    listaAlertas=AlertasModel.objects.all()
    serializer=AlertasSerializer2(listaAlertas,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
   
#--------------------------------------

def crearAlertaVT():
    countLocalizado=getAllCountLocalizado()
    if countLocalizado[0]>=30:
        eventoMacro=getEventoMacroId(countLocalizado[1])
        alerta= AlertasModel(evento=eventoMacro,motivo="Cantidad VT sobre el criterio")
        alerta.save()
        """ return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT) """
#-------------------------------------

def createAlertas(id):
    alerta = AlertasModel(evento=id)
    alerta.save()
    return True
