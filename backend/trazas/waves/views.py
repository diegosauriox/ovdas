import time
import datetime
import numpy as np
#from traces_ufro import *
#from pyrocko import trace
#import pyrocko.gui as gui
#import pyrocko
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
from django.core import serializers
from mysql.connector import Error
import json


@api_view(['GET'])
def algo(request):
    serializer_context = {
        'request': Request(request),
    }
    return Response("xao", status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    print(request.data)
    station_list=request.data.get("nombre")
    date1=request.data.get("fecha_inicio")
    date2=request.data.get("fecha_fin")

    #si no funciona asi escribir: request.data.get("nombre")
    # 
    #  
    #aca llega nombre de estacion
    #station_list=['FRE','CHS','PLA','CHA','ROB',\
     #           'FU2','SHG','NBL','PTZ','PHI','LBN','BI0']



    #stattion=pyrocko.model.station.load_stations('Estaciones_Pyrocko.pf')
    #network='99'
    """ Define tiempo """
    #aca definir tiempo
    #date1='2020-02-18 00:06:00'
    #date1='2020-03-25 11:57:59'
    #date2='2020-02-18 00:10:00'
    #dt1=datetime.datetime.strptime(date1,'%Y-%m-%d %H:%M:%S')
    #dt2=datetime.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')
    #posix_dt1 = time.mktime(dt1.timetuple())-30
    #posix_dt2 = posix_dt1+240 #time.mktime(dt2.timetuple())

    #st_final=[]
    """ Carga trazas de forma remota """
    #st_final=read_stations(st_final,posix_dt1,posix_dt2,station_list,network)
    return Response("hola", status=status.HTTP_200_OK)
#
