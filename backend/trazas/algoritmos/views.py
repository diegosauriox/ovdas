from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import configparser,string,sys,os
from datetime import datetime
from .UpdateEtiqueta import Clasificador_Multiestacion_Final
from multiprocessing import Process
import subprocess
from subprocess import check_output
from django.core.exceptions import ObjectDoesNotExist

@api_view(['POST'])
def executeAgoritmos(request):
    print(request.data['algoritmo'])
    if request.data['algoritmo'] == 1:
        return executeRegistros(request.data)
    elif request.data['algoritmo'] == 2:
        return executeRegistros(request.data)
    elif request.data['algoritmo'] == 3:
        return executeAlgoAlejandro(request.data)
    elif request.data['algoritmo'] == 4:
        return executeParamFis(request.data)
    elif request.data['algoritmo'] == 0:
        return executeIdenti(request.data)
    else:
        Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def executeIdenti(datos):
    date_time_obj = datetime.strptime(datos['fechaIni'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaIncio = date_time_obj.toordinal()
    date_time_obj = datetime.strptime(datos['fechaFin'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaFin = date_time_obj.toordinal()

    t_ini = str(fechaIncio)
    t_fin = str(fechaFin)

    cfgfile = open('algoritmos/' + "clasi.conf", 'w+')

    Config = configparser.ConfigParser()
    Config.add_section('Temporal_request')
    Config.set('Temporal_request', 't_ini', t_ini)
    Config.set('Temporal_request', 't_fin', t_fin)

    Config.write(cfgfile)
    cfgfile.close()
    return Response(status=status.HTTP_200_OK)


def executeRegistros(datos):
    date_time_obj = datetime.strptime(datos['fechaIni'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaIncio = date_time_obj.toordinal()
    date_time_obj = datetime.strptime(datos['fechaFin'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaFin = date_time_obj.toordinal()

    t_ini = str(fechaIncio)
    t_fin = str(fechaFin)

    cfgfile = open('algoritmos/' + "clasi.conf", 'w+')

    Config = configparser.ConfigParser()
    Config.add_section('Temporal_request')
    Config.set('Temporal_request', 't_ini', t_ini)
    Config.set('Temporal_request', 't_fin', t_fin)

    Config.write(cfgfile)
    cfgfile.close()
    return Response(status=status.HTTP_200_OK)

def executeLocali(datos):

    date_time_obj = datetime.strptime(datos['fechaIni'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaIncio = date_time_obj.toordinal()
    date_time_obj = datetime.strptime(datos['fechaFin'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaFin = date_time_obj.toordinal()

    t_ini = str(fechaIncio)
    t_fin = str(fechaFin)

    cfgfile = open('algoritmos/' + "clasi.conf", 'w+')

    Config = configparser.ConfigParser()
    Config.add_section('Temporal_request')
    Config.set('Temporal_request', 't_ini', t_ini)
    Config.set('Temporal_request', 't_fin', t_fin)

    Config.write(cfgfile)
    cfgfile.close()
    return Response(status=status.HTTP_200_OK)


def executeAlgoAlejandro(datos):
    print(datos)
    date_time_obj = datetime.strptime(datos['fechaIni'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaIncio =  date_time_obj.toordinal()
    date_time_obj = datetime.strptime(datos['fechaFin'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaFin = date_time_obj.toordinal()

    ip = '143.198.234.8'
    port = '3306'
    user = 'teamRegistro'
    password = 'regiStro753'
    db = 'ufro_ovdas_v1'
    table_iden = 'identificacion_senal'

    #[Temporal_request]
    # string como identificacion tanto para t_ini y t_fin
    t_ini = str(fechaIncio)
    t_fin = str(fechaFin)

    #[Confiabilidad_estaciones]
    FRE = '0.99'
    SHG = '0.98'
    LBN = '0.97'
    PTZ = '0.96'
    NBL = '0.95'
    CHS = '0.94'
    FU2 = '0.93'
    PHI = '0.92'
    PLA = '0.91'
    ROB = '0.90'

    cfgfile = open('algoritmos/UpdateEtiqueta/' + "clasi.conf", 'w+')

    # add the settings to the structure of the file, and lets write it out...i
    Config = configparser.ConfigParser()
    Config.add_section('Database')
    Config.set('Database', 'ip', ip)
    Config.set('Database', 'port', port)
    Config.set('Database', 'user', user)
    Config.set('Database', 'password', password)
    Config.set('Database', 'db', db)
    Config.set('Database', 'table_iden', table_iden)


    Config.add_section('Temporal_request')
    Config.set('Temporal_request', 't_ini', t_ini)
    Config.set('Temporal_request', 't_fin', t_fin)

    Config.add_section('Confiabilidad_estaciones')
    Config.set('Confiabilidad_estaciones', 'FRE', FRE)
    Config.set('Confiabilidad_estaciones', 'SHG', SHG)
    Config.set('Confiabilidad_estaciones', 'LBN', LBN)
    Config.set('Confiabilidad_estaciones', 'PTZ', PTZ)
    Config.set('Confiabilidad_estaciones', 'NBL', NBL)
    Config.set('Confiabilidad_estaciones', 'CHS', CHS)
    Config.set('Confiabilidad_estaciones', 'FU2', FU2)
    Config.set('Confiabilidad_estaciones', 'PHI', PHI)
    Config.set('Confiabilidad_estaciones', 'PLA', PLA)
    Config.set('Confiabilidad_estaciones', 'ROB', ROB)

    Config.write(cfgfile)
    cfgfile.close()

    if Clasificador_Multiestacion_Final.executeMain():
        return Response('Ejecutado',status=status.HTTP_202_ACCEPTED)
    else:
        Response(status=status.HTTP_409_CONFLICT)


def executeParamFis(datos):
    date_time_obj = datetime.strptime(datos['fechaIni'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaIncio = date_time_obj.toordinal()
    date_time_obj = datetime.strptime(datos['fechaFin'][:19], '%Y-%m-%dT%H:%M:%S')
    fechaFin = date_time_obj.toordinal()

    t_ini = str(fechaIncio)
    t_fin = str(fechaFin)

    cfgfile = open('algoritmos/' + "clasi.conf", 'w+')

    Config = configparser.ConfigParser()
    Config.add_section('Temporal_request')
    Config.set('Temporal_request', 't_ini', t_ini)
    Config.set('Temporal_request', 't_fin', t_fin)

    Config.write(cfgfile)
    cfgfile.close()
    return Response(status=status.HTTP_200_OK)