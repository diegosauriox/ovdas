from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EventoMacroModel
from .serializers import EventoMacroSerializer
from estaciones.views import estacioneByVolcan as estacionByVolcan
from eventoLocali.models import EventoLocalizadoModel
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.core import serializers
from mysql.connector import Error
import json
import locale


# Create your viewss here.
@api_view(['GET'])
def index(request):
    eventoMacros = EventoMacroModel.objects.all()[:5]
    eventoMacros2 = EventoMacroModel.objects.filter(eventolocalizadomodel__isnull=True).values_list('evento_macro_id')[:5]
    datos = []
    for evento in eventoMacros2:
        locali = EventoLocalizadoModel.objects.get(evento_macro_id=evento)
        #print(evento.eventolocalizadomodel)
        datos.append(locali)
    print(eventoMacros2.query)

    #serializer = EventoMacroSerializer(eventoMacros, many=True)
    #data = serializers.serialize('json', eventoMacros2)
    return HttpResponse(eventoMacros2, content_type="application/json")
    #return JsonResponse(eventoMacros2, safe=False)

@api_view(['GET'])
def getEstacionesByEventoMacro(request,id):
    eventoMacro= EventoMacroModel.objects.get(evento_macro_id=id)
    estaciones= estacionByVolcan(eventoMacro.volcan_id)
    return Response(estaciones, status=status.HTTP_200_OK)


def getEstacionesByEventoMacroById(id):
    eventoMacro= EventoMacroModel.objects.get(evento_macro_id=id)
    
    datos= {"volcanid":eventoMacro.volcan_id, "clasificacion": eventoMacro.clasificacion}
    return datos

def getEventoMacroId(id):
    eventoMacro= EventoMacroModel.objects.get(evento_macro_id=id)
    return eventoMacro


@api_view(['POST'])
def create(request):
    serializer = EventoMacroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def show(request, id):
    evento = EventoMacroModel.objects.get(id_evento_macro=id)
    print(evento.volcan_id)
    serializer = EventoMacroSerializer(evento, many=True)
    return HttpResponse(serializer)

def validador(id):
    if(EventoMacroModel.objects.filter(evento_macro_id=id).exists()):
        return True
    else:
        return False

def createInternal(volcan_id, macro_evento, fecha_inicio, fecha_termino):
    eve = EventoMacroModel(evento_macro_id=macro_evento, volcan_id=volcan_id, inicio=fecha_inicio, fin=fecha_termino )
    eve.save()
    return True

@api_view(["PUT"])
def update(request, id):
    try:
        estacionAux = EventoMacroModel.objects.get(id_evento_macro=id)
        serializer = EventoMacroSerializer(data=request.data, instance=estacionAux)
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
        estacion = EventoMacroModel.objects.get(id_evento_macro=id)
        estacion.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)

def updateOnlyEtiqueta(data, id):
    try:
        eventoMacro = EventoMacroModel.objects.get(evento_macro_id=id)
        eventoMacro.clasificacion = data
        eventoMacro.save()
        return True
    except ObjectDoesNotExist as e:
        False


def getIdVolcanByEventoMacho(id):
    eventoMacro = EventoMacroModel.objects.get(evento_macro_id=id)
    # datos = {"volcanid": eventoMacro.volcan_id, "clasificacion": eventoMacro.clasificacion}
    return eventoMacro.volcan_id

@api_view(['GET'])
def getCantidadEventosPorMes(request):
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    eventoMacro = EventoMacroModel.objects.filter(created_at__year=currentYear, created_at__month=currentMonth)
    print(eventoMacro.count())
    serializer = EventoMacroSerializer(eventoMacro, many=True)

    return Response(serializer.data)

def getCantidadEventosPorMesVT():
    mesActual = datetime.now()
    now = datetime.now()
    locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))
    eventos = []
    for _ in range(0, 5):
        eventoMacro = EventoMacroModel.objects.filter(created_at__month=mesActual.month, clasificacion='VT')
        evento = {}
        evento['mes'] = now.strftime("%B")
        evento['cantidad'] = eventoMacro.count()
        mesActual = mesActual - relativedelta(months=1)
        now = now.replace(day=1) - timedelta(days=1)
        eventos.append(evento)
    eventos = eventos[::-1]
    return eventos

def getCantidadEventosPorMesLP():
    mesActual = datetime.now()
    now = datetime.now()
    locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))
    eventos = []
    for _ in range(0, 5):
        eventoMacro = EventoMacroModel.objects.filter(created_at__month=mesActual.month, clasificacion='LP')
        evento = {}
        evento['mes'] = now.strftime("%B")
        evento['cantidad'] = eventoMacro.count()
        mesActual = mesActual - relativedelta(months=1)
        now = now.replace(day=1) - timedelta(days=1)
        eventos.append(evento)
    eventos = eventos[::-1]
    return eventos

def getEventosPorMes():
    mesActual = datetime.now()
    now = datetime.now()
    locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))
    eventos = []
    for _ in range(0, 5):
        eventoMacro = EventoMacroModel.objects.filter(created_at__month=mesActual.month)
        evento = {}
        evento['mes'] = now.strftime("%B")
        evento['cantidad'] = eventoMacro.count()
        mesActual = mesActual - relativedelta(months=1)
        now = now.replace(day=1) - timedelta(days=1)
        eventos.append(evento)
    eventos = eventos[::-1]
    #//////NO BORRAR//////
    #eventoMacro = EventoMacroModel.objects.filter(clasificacion='LP').annotate(month=TruncMonth('created_at')).values('month').annotate(c=Count('evento_macro_id')).values('month', 'c')[:12]
    # //////NO BORRAR//////
    return eventos

def getCantidadesResumenMes():
    mesActual = datetime.now()
    #vt = EventoMacroModel.objects.filter(created_at__month=mesActual.month, clasificacion='VT')

@api_view(['GET'])
def resumenDash(request):
    locale.setlocale(locale.LC_ALL, ("es_ES", "UTF-8"))
    mesActual = datetime.now()
    #conteo de eventos simple
    todos = EventoMacroModel.objects.filter(created_at__month=mesActual.month)
    vt = EventoMacroModel.objects.filter(created_at__month=mesActual.month, clasificacion='VT')
    lp = EventoMacroModel.objects.filter(created_at__month=mesActual.month, clasificacion='LP')
    tr = EventoMacroModel.objects.filter(created_at__month=mesActual.month, clasificacion='TR')
    localizaciones = EventoLocalizadoModel.objects.filter(created_at__month=mesActual.month)
    conteoResumen = {'todos': todos.count(), 'vt': vt.count(), 'lp': lp.count(), 'tr': tr.count(), 'localizaciones': localizaciones}

    #CONTEO DE EVENTOS POR MES

    now = datetime.now()
    dashboard = []
    arrEventosMacro = []
    arrEventosVT = []
    arrEventosLP = []
    arrEventosTR = []
    for _ in range(0, 12):
        eventoMacro = EventoMacroModel.objects.filter(created_at__month=mesActual.month)
        eventoVT = EventoMacroModel.objects.filter(created_at__month=mesActual.month, clasificacion='VT')
        eventoLP = EventoMacroModel.objects.filter(created_at__month=mesActual.month, clasificacion='LP')
        eventoTR = EventoMacroModel.objects.filter(created_at__month=mesActual.month, clasificacion='TR')
        objMacro = {}
        objVT = {}
        objLP = {}
        objTR = {}
        objMacro['mes'] = now.strftime("%B")
        objVT['mes'] = now.strftime("%B")
        objLP['mes'] = now.strftime("%B")
        objTR['mes'] = now.strftime("%B")
        objMacro['cantidad'] = eventoMacro.count()
        objVT['cantidad'] = eventoVT.count()
        objLP['cantidad'] = eventoLP.count()
        objTR['cantidad'] = eventoTR.count()
        mesActual = mesActual - relativedelta(months=1)
        now = now.replace(day=1) - timedelta(days=1)
        arrEventosMacro.append(objMacro)
        arrEventosVT.append(objVT)
        arrEventosLP.append(objLP)
        arrEventosTR.append(objTR)
    print(conteoResumen)
    eventosMes = {}
    eventosMes['eventosMacro'] = arrEventosMacro[::-1]
    eventosVT = {}
    eventosVT['eventosVT'] = arrEventosVT[::-1]
    eventosLP = {}
    eventosLP['eventosLP'] = arrEventosLP[::-1]
    eventosTR = {}
    eventosTR['eventosTR'] = arrEventosTR[::-1]
    conteo = {}
    conteo['conteoResumen'] = conteoResumen

    dashboard.append(eventosMes)
    dashboard.append(eventosVT)
    dashboard.append(eventosLP)
    dashboard.append(eventosTR)
    dashboard.append(conteoResumen)
    return Response(dashboard)

