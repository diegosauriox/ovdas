from django.http import JsonResponse
import time
from datetime import datetime
import numpy as np
from avistamientoRegistro.views import getAvistamientoByMacroId
from eventoMacro.views import getEventoMacroId
from identificacion.views import getEstacionByCodeEvent

from waves.traces_ufro import *
from pyrocko import trace
import pyrocko.gui as gui
import pyrocko
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
from eventoMacro.models import EventoMacroModel
from estaciones.views import estacioneByVolcan as estacionByVolcan, getAll
import os 
from datetime import datetime
from obspy.clients.earthworm import Client
from obspy import UTCDateTime
ruta=os.getcwd()+"/waves/Estaciones_Pyrocko.pf"


@api_view(['GET'])
def nuevoGetTraza(request,id):
    cod_event=getAvistamientoByMacroId(id)
    ti=UTCDateTime(getEventoMacroId(id).inicio)
    tf=UTCDateTime(getEventoMacroId(id).fin)
    
    client = Client("172.16.40.70", 16022,timeout=15)
    fulldata=[]
    #INTENTO QUE FUNCIONA DIEGO TRAER TODAS LAS ESTACIONES CON TRAZAS 
    for i in range(len(cod_event)):
 
        volcan=getEstacionByCodeEvent(cod_event[i]["cod_event"])["volcan"]
        estacion=list(cod_event[i]["cod_event"])
        ts=cod_event[i]["t_s"]
        tp=cod_event[i]["t_p"]
        nombreEstacion=estacion[0]+estacion[1]+estacion[2]
        wave=client.get_waveforms('TC',nombreEstacion+"Z",volcan,'HHZ',ti,tf)
        tiempos=wave[0].times("timestamp")*1000
        datos=wave[0].data
        listaF=[]
        for i in range(len(datos)):
            listaF.append([tiempos[i],datos[i]])
        fulldata.append([listaF,nombreEstacion,ts,tp])
    

    ## Aqui obtenemos el paquete de trazas
    wave=client.get_waveforms('TC','FREZ','99','HHZ',ti,tf )

    wave_fil=wave.filter(type='bandpass',freqmin=0.8,freqmax=12)
    
   
    ###### Aquí haciamos algo que no recuerdo

    """ INTENTO TRAER FECHAS *FUNCIONA
    for i in range(len(estaciones)):
        try:
            wave=client.get_waveforms('TC',estaciones[i]["estacion_id"]+"Z",estaciones[i]["volcan"]["volcan_id"],'HHZ',ti,tf)
            datos=wave[0].data
            fulldata.append([datos,estaciones[i]["estacion_id"]])
        except:

            print(i)
            
    tiempos=wave[0].times("utcdatetime")    
        
    ts=[]
    tiempos2=wave[0].times("timestamp")*1000
    for tiempo in tiempos:
        d=tiempo.datetime
        ts.append(time.mktime(d.timetuple())*1000)
        
    
    datosF=wave[0].data

    listaF=[]
    for i in range(len(datosF)):
        listaF.append([tiempos2[i],datosF[i]])
 """

    return Response(fulldata,status=status.HTTP_200_OK)


@api_view(['GET'])
def algo(request):
    serializer_context = {
        'request': Request(request),
    }
    return Response("xao", status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):   
    # nombre=str(request.data.get('nombre'))
    # fecha=str(request.data.get('hora_inicio'))
    #fecha='11:57:59'
     # nombre=str(request.data.get('nombre'))
    # fecha=str(request.data.get('hora_inicio'))
    # fecha='11:57:59'
    code_event=getAvistamientoByMacroId(request.data[0]['eventoMacroId'])
    estacion=getEstacionByCodeEvent(code_event)
    # print(fecha)

    station_list = [estacion]
    stattion = pyrocko.model.station.load_stations(ruta)
    network = '99'

    """ Define tiempo """
    # date1='2020-02-18 '+ fecha

    date1 = request.data[0]['fecha']
    
    fecha=list(date1)
    fecha[10]="T"
    cambiar=""
    
    # date2='2020-02-18 00:10:00'
    dt1 = datetime.datetime.strptime(cambiar.join(fecha)[:19], '%Y-%m-%dT%H:%M:%S')
    
    #dt1=datetime.datetime.strptime(date1,'%Y-%m-%d %H:%M:%S')
    #dt2=datetime.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')
    
    posix_dt1 = time.mktime(dt1.timetuple())-30 
    posix_dt2 = posix_dt1+120 #time.mktime(dt2.timetuple())

    st_final=[]
    st_tiempo=[]
    """ Carga trazas de forma remota """
    st_final,st_tiempo=read_stations(st_final,st_tiempo,posix_dt1,posix_dt2,station_list,network)
    #0=Z 1=E 2=N
    datosXZ=st_final[0].get_xdata()
    datosYZ=st_final[0].get_ydata()
    #datosXE=st_final[1].get_xdata()
    #datosYE=st_final[1].get_ydata()
    #datosXN=st_final[2].get_xdata()
    #datosYN=st_final[2].get_ydata()
    datos=[]
    lista=[]
    tiempos=[]
    lista.append(datosXZ)
    lista.append(datosYZ)
    aux = '2017-11-24 01:00:22.305'
    for tiempo in st_tiempo:
        #t1 = datetime.datetime.strptime(fecha)
        tiempoAñadir=str(datetime.datetime.fromtimestamp(tiempo))
        tiempos.append(tiempoAñadir[:23])
    if (aux == tiempos[6933]):
        print( 'es igual')

    print(aux)
    print(tiempos[6933])
    print('fecha')
    datos.append(lista)
    datos.append(tiempos)

    

    # lista.append(datosXE)
    # lista.append(datosYE)
    # lista.append(datosXN)
    # lista.append(datosYN)
    #print(tiempos.index('2017-12-12 09:25:04.472'))
    return Response(datos,status=status.HTTP_200_OK)


@api_view(['POST'])
def createByFechaEstacion(request):
# nombre=str(request.data.get('nombre'))
    # fecha=str(request.data.get('hora_inicio'))
    # fecha='11:57:59'

    fecha = request.data['fecha']
    # print(fecha)

    nombre = request.data['est']
    station_list = [nombre]
    stattion = pyrocko.model.station.load_stations(ruta)
    network = '99'

    """ Define tiempo """
    # date1='2020-02-18 '+ fecha

    date1 = request.data['fecha']
    # date2='2020-02-18 00:10:00'
    dt1 = datetime.datetime.strptime(date1[:19], '%Y-%m-%dT%H:%M:%S')

    # dt1=datetime.datetime.strptime(date1,'%Y-%m-%d %H:%M:%S')
    # dt2=datetime.datetime.strptime(date2,'%Y-%m-%d %H:%M:%S')

    posix_dt1 = time.mktime(dt1.timetuple()) - 30
    posix_dt2 = posix_dt1 + 120  # time.mktime(dt2.timetuple())

    st_final = []
    st_tiempo = []
    """ Carga trazas de forma remota """
    st_final, st_tiempo = read_stations(st_final, st_tiempo, posix_dt1, posix_dt2, station_list, network)
    # 0=Z 1=E 2=N
    datosXZ = st_final[0].get_xdata()
    datosYZ = st_final[0].get_ydata()
    # datosXE=st_final[1].get_xdata()
    # datosYE=st_final[1].get_ydata()
    # datosXN=st_final[2].get_xdata()
    # datosYN=st_final[2].get_ydata()
    print(datosXZ)
    datos = []
    lista = []
    tiempos = []
    lista.append(datosXZ)
    lista.append(datosYZ)
    aux = '2017-11-24 01:00:22.305'
    for tiempo in st_tiempo:
        # t1 = datetime.datetime.strptime(fecha)
        tiempoAñadir = str(datetime.datetime.fromtimestamp(tiempo))
        tiempos.append(tiempoAñadir[:23])
    if (aux == tiempos[6933]):
        print('es igual')

    print(aux)
    print(tiempos[6933])
    print('fecha')
    datos.append(lista)
    datos.append(tiempos)

    # lista.append(datosXE)
    # lista.append(datosYE)
    # lista.append(datosXN)
    # lista.append(datosYN)
    # print(tiempos.index('2017-12-12 09:25:04.472'))
    return Response(datos, status=status.HTTP_200_OK)

@api_view(['GET'])
def createAllTrazas(request):
    evento_macro_id=request.data.get('evento_macro_id')
    eventoMacro= EventoMacroModel.objects.get(evento_macro_id=id)
    estaciones= estacionByVolcan(eventoMacro.volcan_id)
    lista=recorrerEstaciones(estaciones,request.data.get('hora'))
    return Response(lista,status=status.HTTP_200_OK)
   
def recorrerEstaciones(estaciones,hora):
    lista=[]
    for estacion in estaciones:
        nombre = estacion.estacion_id
        station_list=[nombre]
        stattion=pyrocko.model.station.load_stations(ruta)
        network='99'
        dt1=datetime.datetime.strptime(hora,'%Y-%m-%d %H:%M:%S')
        posix_dt1 = time.mktime(dt1.timetuple())-30
        posix_dt2 = posix_dt1+0.10
        st_final=[  ]
        st_final=read_stations(st_final,posix_dt1,posix_dt2,station_list,network)
        datosXZ=st_final[0].get_xdata()
        datosYZ=st_final[0].get_ydata()
        lista.append(datosXZ)
        lista.append(datosYZ)
    return lista

