from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import mysql.connector
import time
import csv
from django.core import serializers
from mysql.connector import Error
import json
import pandas as pd
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from eventoMacro.views import *
from identificacion.views import updateProbConf, validador as existIden

from datetime import datetime, date, datetime
from django.utils import timezone

from sqlalchemy.sql.elements import conv

class MyUploadView(viewsets.ModelViewSet):
    parser_class = (FileUploadParser,)
    queryset = 0
    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']
        # guardar o procesar el archivo
        # mymodel.my_file_field.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def loadVolcanesCSV(request):
    file = request.body

    jsonfile = json.loads(file)
    ser = pd.read_json(file, lines=False, typ='series')
    print(ser)
    ser.to_csv('datasetexternal/filesDataSet/volcanes.csv', index=1, header=False)
    data = pd.read_csv('datasetexternal/filesDataSet/volcanes.csv', engine='python', sep=';', encoding='utf-8', error_bad_lines=False)
    df = pd.DataFrame(data, columns=['file1,"﻿id_volcan', 'nombre', 'descripcion', 'latitud', 'longitud', 'altura'])
    print(df)
    connection = mysql.connector.connect(host='localhost',
                                         database='ufro_ovdas',
                                         user='root',
                                         password='')

    cursor = connection.cursor()
    print(df)
    # Insert DataFrame to Table
    for row in df.itertuples():
        print(row[0])
        cursor.execute('''
                            INSERT INTO volcan (id_volcan, nombre, descripcion, latitud, longitud, altura)
                            VALUES (%s,%s,%s,%s,%s,%s)
                            ''',
                       (row[1],
                        row.nombre,
                        row.descripcion,
                        row.latitud,
                        row.longitud,
                        row.altura
                        )
                       )
    connection.commit()
    return Response('funciono', status=status.HTTP_200_OK)


@api_view(['POST'])
def updateIndentificacionMacroCSV(request):
    file = request.body
    #jsonfile = json.loads(file)
    ser = pd.read_json(file, lines=False, typ='series')
    print(ser)
    ser.to_csv('datasetexternal/filesDataSet/updateEtiqueta.csv', index=1, header=False)
    data = pd.read_csv('datasetexternal/filesDataSet/updateEtiqueta.csv', engine='python', sep=';', encoding='utf-8', error_bad_lines=False)
    df = pd.DataFrame(data, columns=['file1,"code_macroevent', 'code_event', 'class_macroevent', 'prob_class', 'conf'])
    print(df)
    errores = 0
    # Insert DataFrame to Table
    for row in df.itertuples():
        if(validador(row[1]) & existIden(row.code_event)):
            updateOnlyEtiqueta(row.class_macroevent, row[1])
            updateProbConf(row.code_event, row.prob_class, row.conf)
            #print('carga para' + row.class_macroevent + row[1])
            # Actualiza la etiqueta del macro evento
        else:
            errores += 1
            #return Response('Error al cargar los datos', status=status.HTTP_400_BAD_REQUEST)
            #print('no econtro datos')
    return Response('Datos actualizados,'+ ' no ha cargado '+ str(errores), status=status.HTTP_200_OK)

@api_view(['POST'])
def loadLocalizacionesCSV(request):
    file = request.body
    #jsonfile = json.loads(file)
    ser = pd.read_json(file, lines=False, typ='series')
    print(ser)
    ser.to_csv('datasetexternal/filesDataSet/localizaciones.csv', index=1, header=False)
    data = pd.read_csv('datasetexternal/filesDataSet/localizaciones.csv', engine='python', sep=';', encoding='utf-8', error_bad_lines=False)
    df = pd.DataFrame(data, columns=['code_macroevent', 'tiempo_origen', 'lat', 'lon', 'z', 'rmse', 'major_half_axes', 'minor_half_axes', 'dz', 'gap', 'ml', 'n_fases', 'descrip', 'autor'])
    print(df)



    print(df)
    # Insert DataFrame to Table
    for row in df.itertuples():
            print(row)
            print(row[0])
            if(validador(row.code_macroevent)):
                connection = mysql.connector.connect(host='localhost',
                                                     database='ufro_ovdas_v1',
                                                     user='root',
                                                     password='')
                cursor = connection.cursor()
                cursor.execute('''
                                    INSERT INTO evento_localizado (evento_macro_id, tiempo, lat, lon, z, rmse, major_half_axes, minor_half_axes, dz, gap, ml, n_fases, descrip, autor, created_at)
                                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                    ''',
                               (row.code_macroevent,
                                row.tiempo_origen,
                                row.lat,
                                row.lon,
                                row.z,
                                row.rmse,
                                row.major_half_axes,
                                row.minor_half_axes,
                                row.dz,
                                row.gap,
                                row.ml,
                                row.n_fases,
                                row.descrip,
                                row.autor,
                                datetime.now(timezone.utc).timestamp()
                                )
                               )
                connection.commit()
    return Response('funciono', status=status.HTTP_200_OK)

@api_view(['POST'])
def loadIdentificacionSenalCSV(request):
    file = request.body
    # jsonfile = json.loads(file)
    ser = pd.read_json(file, lines=False, typ='series')
    ser.to_csv('datasetexternal/filesDataSet/identificiones.csv', index=1, header=False)
    data = pd.read_csv('datasetexternal/filesDataSet/identificiones.csv', engine='python', sep=';', encoding='utf-8',
                       error_bad_lines=False)

    df = pd.DataFrame(data, columns=['file1,"cod_event', 'cod_event_in', 'volcan', 'est', 'componente', 'id_cl', 'fecha_pick', 'analista', 'snr', 'label_event', 'c_label', 'descripcion', 'prom_ruido_fondo', 'inicio', 'fin', 'largo', 'prob_vt', 'prob_lp', 'prob_tr', 'prob_ot'])

    print(df)
    # Insert DataFrame to Table
    for row in df.itertuples():
        print(row.index)
        if(False == existIden(row[1])):
            connection = mysql.connector.connect(host='localhost',
                                                 database='ufro_ovdas_v1',
                                                 user='root',
                                                 password='')
            cursor = connection.cursor()
            cursor.execute('''
                            INSERT INTO identificacion_senal (cod_event, cod_event_in, volcan, est, componente, cl_id, algo_detecion_id, fecha_pick, analista, snr, label_event, c_label, created_at, descripcion, prom_ruido_fondo, inicio, fin, largo, prob_vt, prob_lp, prob_tr, prob_ot)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            ''',
                           (row[1], # obtiene el valor de file1,"cod_event
                            row.cod_event_in,
                            row.volcan,
                            row.est,
                            row.componente,
                            1,
                            row.id_cl,
                            row.fecha_pick,
                            row.analista,
                            row.snr,
                            row.label_event,
                            row.c_label,
                            timezone.now(),
                            row.descripcion,
                            row.snr,
                            row.inicio,
                            row.fin,
                            row.largo,
                            row.prob_vt,
                            row.prob_lp,
                            row.prob_tr,
                            row.prob_ot)
                           )
            connection.commit()

    return Response('funciono', status=status.HTTP_200_OK)

@api_view(['POST'])
def loadRegistroCSV(request):
    file = request.body

    ser = pd.read_json(file, lines=False, typ='series')
    ser.to_csv('datasetexternal/filesDataSet/registro.csv', index=1, header=False)
    data = pd.read_csv('datasetexternal/filesDataSet/registro.csv', engine='python', sep=';', encoding='utf-8',
                       error_bad_lines=False)

    df = pd.DataFrame(data, columns=['componente', 'code_event', 'code_macroevent', 'file1,"cod_event_in', 'id_tecnica', 'fecha_pick', 'autor', 't_p', 't_s', 'c_p', 'c_s', 'inicio', 'snr', 'polar', 'descrip', 'label_event', 'amplitud', 'coda', 'frecuencia', 'id_volcan'])
    print(df)
    connection = mysql.connector.connect(host='localhost',
                                         database='ufro_ovdas_v1',
                                         user='root',
                                         password='')


    print(df)
    # Insert DataFrame to Table
    for row in df.itertuples():
        # evualuar si existe evento macro, sino crearlo.
        # usar find de modelos para macro envento
        print(row)
        estado = False
        if (validador(row.code_macroevent)):
            print('si existe la row')
        else:
             #crear evento macro
            print('crea evento macro')
            createInternal(row.id_volcan, row.code_macroevent, row.inicio, row.inicio)
            print('termina de crear evento macro')
            if(existIden(row.code_event)):
                cursor = connection.cursor()
                cursor.execute('''
                                    INSERT INTO avistamiento_registro (cod_event, cod_event_in, evento_macro_id, t_p, t_s, coda, c_p, c_s, c_coda, inicio, polar, frecuencia, amplitud, autor, label_event, descripcion, componente, snr, tecnica_id, fecha_pick, created_at)
                                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                    ''',
                                   (row.code_event,
                                    row[0],
                                    row.code_macroevent,
                                    row.t_p,
                                    row.t_s,
                                    row.coda,
                                    row.c_p,
                                    row.c_s,
                                    1,
                                    row.inicio,
                                    row.polar,
                                    row.frecuencia,
                                    row.amplitud,
                                    row.autor,
                                    row.label_event,
                                    row.descrip,
                                    row.componente,
                                    row.snr,
                                    row.id_tecnica,
                                    row.fecha_pick,
                                    time.strftime("%c"))
                                   )
                connection.commit()
            else:
                print('no econtro evento en indentificaciones')

    return Response('funciono', status=status.HTTP_200_OK)

def createEventoMacro(volcan_id, macro_evento, fecha_inicio, fecha_fermino):

    try:
        # alamacenar los datos de evento macro
        return True
    except Exception as e:
        #error
        return False

