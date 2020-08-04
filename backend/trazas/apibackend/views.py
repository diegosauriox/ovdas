import zipfile
from urllib import response
import mysql.connector
from mysql.connector import Error
from obspy import read
from django.shortcuts import render

# Create your viewss here.
from requests import request

from django.http import JsonResponse, HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from .viewss import *

from . import serializers
from .serializers import FrezHhzTc9920200321Serializer
from .models import FrezHhzTc9920200321


class TrazaViewSet(viewsets.ModelViewSet):
    # queryset = FrezHhzTc9920200321.objects.all().order_by('st')
    queryset = FrezHhzTc9920200321.objects.all().order_by('st')[:10]
    serializer_class = FrezHhzTc9920200321Serializer


class Test2():
    response_data = JsonResponse({'foo':'bar'})
    queryset = FrezHhzTc9920200321.objects.all().order_by('st')[:10]
    serializer_class = FrezHhzTc9920200321Serializer


@api_view(['GET', 'POST'])
def test(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles': ['Admin', 'User'],
        'tracebuf' : ''
    }
    connection = mysql.connector.connect(host='localhost',
                                         database='ufro_ovdas',
                                         user='root',
                                         password='')

    cursor = connection.cursor()
    sql_fetch_blob_query = """SELECT * from volcan  limit 1"""
    cursor.execute(sql_fetch_blob_query)
    record = cursor.fetchall()
    #record.decode('utf-8')

    #st4 = read(record[0][0].decode('latin1'))

    #print(st4)
    #st1.plot()
    #st1.plot(outfile='singlechannel.png')
    
    #consulta = FrezHhzTc9920200321.objects.raw('''SELECT 'tracebuf' FROM frez$hhz$tc$99$$2020_03_21 WHERE st = '638020800.9683928' limit 1  ''')
    #response = FrezHhzTc9920200321.objects.raw('SELECT "tracebuf" FROM frez$hhz$tc$99$$2020_03_21 WHERE st = "638020800.9683928" limit 1')
    #responseData['st'] = consulta
    #data = consulta
    #response = JsonResponse(consulta)
    #response = consulta
    #data = serializers.serialize('json', FrezHhzTc9920200321)
    blob_content = b''


    return HttpResponse(record[0][0], content_type="application/json")
    #return JsonResponse(blob_content)