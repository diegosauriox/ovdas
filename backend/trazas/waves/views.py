from django.http import JsonResponse
import time
import datetime
import numpy as np
from waves.traces_ufro import *
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

@api_view(['GET'])
def create(request):
    
    # nombre=str(request.data.get('nombre'))
    # fecha=str(request.data.get('hora_inicio'))
    fecha='11:57:59'
    nombre='FRE'
    station_list=[nombre]

    stattion=pyrocko.model.station.load_stations('/home/diego/Escritorio/ovdas/backend/trazas/waves/Estaciones_Pyrocko.pf')
    network='99'


    

    """ Define tiempo """
    date1='2020-02-18 '+ fecha
    #date1='2020-03-25 11:57:59'
    #date2='2020-02-18 00:10:00'
    dt1=datetime.datetime.strptime(date1,'%Y-%m-%d %H:%M:%S')
    #dt2=datetime.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')
    posix_dt1 = time.mktime(dt1.timetuple())-30 
    posix_dt2 = posix_dt1+0.10 #time.mktime(dt2.timetuple())

    st_final=[  ]
    """ Carga trazas de forma remota """
    st_final=read_stations(st_final,posix_dt1,posix_dt2,station_list,network)
    #0=Z 1=E 2=N
    datosXZ=st_final[0].get_xdata()
    datosYZ=st_final[0].get_ydata()
    datosXE=st_final[1].get_xdata()
    datosYE=st_final[1].get_ydata()
    datosXN=st_final[2].get_xdata()
    datosYN=st_final[2].get_ydata()
    lista=[]
    lista.append(datosXZ)
    lista.append(datosYZ)
    # lista.append(datosXE)
    # lista.append(datosYE)
    # lista.append(datosXN)
    # lista.append(datosYN)
    return Response(lista,status=status.HTTP_200_OK)
    
#
