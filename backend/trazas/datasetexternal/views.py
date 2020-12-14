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
from django.core import serializers
from mysql.connector import Error
import json
import pandas as pd
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage


# Create your viewss here.
from sqlalchemy.sql.elements import conv


@api_view(['POST'])
def loadVolcanesCSV(request):
    print(request.files)
    print('llega')
    file = request.data
    file_name = default_storage.save('prueba', file)
    #form = UploadFileForm(request.POST, request.FILES)
    fs = FileSystemStorage()
    #filename = fs.save(myfile.name, myfile)
    fs.url('prueba')

    #estaciones = EstacionModel.objects.all()
    #serializer = EstacionSerializer(estaciones, many=True )
    return Response('funciono', status=status.HTTP_200_OK)

@api_view(['GET'])
def loadIdentificacionSenalCSV(request):
    #data= pd.read_csv(r'/home/diego/Escritorio', sep=';')
    #df = pd.DataFrame(data, columns=['nombre', 'altura'])

    df = pd.DataFrame(data, columns=['cod_event_in', 'volcan', 'est', 'componente', 'id_cl', 'id_det', 'fecha_pick', 'analista', 'snr', 'label_event', 'c_label', 'descripcion', 'prom_ruido_fond', 'inicio', 'fin'])
    connection = mysql.connector.connect(host='localhost',
                                         database='ufro_ovdas',
                                         user='root',
                                         password='')

    cursor = connection.cursor()
    print(df)
    # Insert DataFrame to Table
    for row in df.itertuples():
        print(row.prom_ruido_fond)
        cursor.execute('''
                        INSERT INTO indentificacion_senal (cod_event_in, volcan, est, componente, id_cl, id_det, fecha_pick, analista, snr, label_event, c_label, created_at, descripcion, prom_ruido_fondo, inicio, fin)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        ''',
                       (row.cod_event_in,
                        row.volcan,
                        row.est,
                        row.componente,
                        row.id_cl,
                        row.id_det,
                        row.fecha_pick,
                        row.analista,
                        row.snr,
                        row.label_event,
                        row.c_label,
                        time.strftime("%c"),
                        row.descripcion,
                        row.prom_ruido_fond,
                        row.inicio,
                        row.fin)
                       )
    connection.commit()

    return Response('funciono', status=status.HTTP_200_OK)

@api_view(['POST'])
def loadLocalizacionesCSV(request):
    file = request.body

    #jsonfile = json.loads(file)
    ser = pd.read_json(file, lines=False, typ='series')
    print(ser)
    ser.to_csv('datasetexternal/filesDataSet/localizaciones.csv', index=1, header=False)
    data = pd.read_csv('datasetexternal/filesDataSet/localizaciones.csv', engine='python', sep=';', encoding='utf-8', error_bad_lines=False)
    df = pd.DataFrame(data, columns=['file1,"﻿id_evento_macro', 'tiempo', 'lat', 'lon', 'z', 'rmse', 'major_half_axes', 'minor_half_axes', 'dz', 'gap', 'ml', 'n_fases', 'descrip', 'autor'])
    print(df)
    connection = mysql.connector.connect(host='localhost',
                                         database='ufro_ovdas',
                                         user='diego',
                                         password='beyblade1')

    cursor = connection.cursor()
    print(df)
    # Insert DataFrame to Table
    for row in df.itertuples():
        print(row[0])
        cursor.execute('''
                            INSERT INTO evento_localizado (id_evento_macro, tiempo, lat, lon, z, rmse, major_half_axes, minor_half_axes, dz, gap, ml, n_fases, descrip, autor, created_at)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            ''',
                       (row[1],
                        row.tiempo,
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
                        time.strftime("%c")
                        )
                       )
    connection.commit()
    return Response('funciono', status=status.HTTP_200_OK)