from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
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
def obtenerAlertas(request, id):
    #alertas = AlertasModel.objects.all()
    alertas = AlertasModel.objects.select_related('evento')
    print(alertas.query)
    #alertas = AlertasModel.filter(eventob__isnull=False)
    #serializer = AlertasSerializer(alertas, many=True)
    datosAlertas=[]
    '''for alerta in alertas:
        datos=getEstacionesByEventoMacroById(alerta.evento_id)""" me trae el id volcan y la clasificacion"""
        clasificacion=datos.clasificacion
        volcan_id=datos.volcan_id
        nombreVolcan=getNombreVolcanById(volcan_id)
        ml=getMlById(alerta.evento_id)
        datosAlerta.append({volcan:nombreVolcan,ml:ml,clasificacion:clasificacion,tiempo:alerta.created_at})'''
    #return HttpResponse(alertas, status=status.HTTP_200_OK)
    qs_json = serializers.serialize('json', alertas)
    return HttpResponse(qs_json, content_type='application/json')
# Create your views here.

