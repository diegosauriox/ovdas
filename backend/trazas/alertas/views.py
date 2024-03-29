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
from paramDiscrFisc.views import getMlbyMacroId, recorrerParametros as recorrerParametros
from paramDiscrFisc.views import getParametrosEntreFechas as getParametrosEntreFechas
from paramDiscrFisc.views import getAll as getParametrosAll
from eventoMacro.models import EventoMacroModel
from criterioAlerta.views import getUmbralDR as getUmbralDR
from criterioAlerta.views import getUmbralML as getUmbralML
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
         
        datos=getEstacionesByEventoMacroById(alerta.evento_id)     
        clasificacion=datos["clasificacion"]
        
        volcan_id=datos["volcanid"]
        nombreVolcan=getNombreVolcanById(volcan_id) 
        ml=getMlbyMacroId(alerta.evento_id)
        tiempoIni=getEventoMacroId(alerta.evento_id).inicio
        eventoMacro=alerta.evento_id
        #print(tiempoIni.inicio)
        datosAlerta.append({"volcan":nombreVolcan,"evento_macro_id":eventoMacro,"tiempoIni":tiempoIni,"ml":ml,"clasificacion":clasificacion,"motivo":alerta.motivo,"tiempo":alerta.created_at}) 
        #print (datosAlerta)
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

def crearAlertasMlDr(t1,t2):

    parametros = getParametrosEntreFechas(t1,t2)
    for parametro in parametros:
        criterioDr=getUmbralDR(parametro["evento_macro"]["volcan_id"])
        criterioMl=getUmbralML(parametro["evento_macro"]["volcan_id"])
        if(parametro["ml"]>=criterioMl):
            eventoMacro=getEventoMacroId(parametro["evento_macro"]["evento_macro_id"])  
            alerta= AlertasModel(evento=eventoMacro,motivo="Cantidad Ml sobre el criterio")
            alerta.save()
        if(parametro["dr_c"]>=criterioDr):
            eventoMacro=getEventoMacroId(parametro["evento_macro"]["evento_macro_id"])  
            alerta= AlertasModel(evento=eventoMacro,motivo="Cantidad Dr sobre el criterio")
            alerta.save()


def crearTodasAlertasMlDr():
    parametros = getParametrosAll()
    for parametro in parametros:
        criterioDr=getUmbralDR(parametro["evento_macro"]["volcan_id"])
        criterioMl=getUmbralML(parametro["evento_macro"]["volcan_id"])
        if(parametro["ml"]>=criterioMl):
            eventoMacro=getEventoMacroId(parametro["evento_macro"]["evento_macro_id"])  
            alerta= AlertasModel(evento=eventoMacro,motivo="Cantidad Ml sobre el criterio")
            alerta.save()
        if(parametro["dr_c"]>=criterioDr):
            eventoMacro=getEventoMacroId(parametro["evento_macro"]["evento_macro_id"])  
            alerta= AlertasModel(evento=eventoMacro,motivo="Cantidad Dr sobre el criterio")
            alerta.save()
#-------------------------------------

def createAlertas(id):
    alerta = AlertasModel(evento=id)
    alerta.save()
    return True

@api_view(['GET'])
def getAlertasDash(request):
    eventoMacros = EventoMacroModel.objects.filter(parmfisdiscretomodel__isnull=True, volcan__isnull=False, eventolocalizadomodel__isnull=True).values('evento_macro_id',
                                                                'clasificacion', 'volcan_id', 'inicio',
                                                                'parmfisdiscretomodel__ml',
                                                                'parmfisdiscretomodel__dr_c',
                                                                'volcan__nombre',
                                                                'eventolocalizadomodel__lon',
                                                                'eventolocalizadomodel__lat', 'eventolocalizadomodel__z').distinct()
    alertas = AlertasModel.objects.filter(evento__parmfisdiscretomodel__isnull=False, evento__volcan__isnull=False).values('evento_id', 'evento__clasificacion', 'evento__parmfisdiscretomodel__ml', 'evento__parmfisdiscretomodel__dr_c',
                                            'evento__parmfisdiscretomodel', 'evento__parmfisdiscretomodel__energia', 'evento__parmfisdiscretomodel__freq',  'evento__volcan__nombre', 'evento__eventolocalizadomodel__z',
                                            'evento__eventolocalizadomodel__lat', 'evento__eventolocalizadomodel__lon').distinct()
    print(alertas.query)
    return Response(alertas, status=status.HTTP_200_OK)