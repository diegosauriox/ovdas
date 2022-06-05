from eventoMacro.views import getEventoMacroId
from datetime import date, datetime, timedelta
from .models import ParmFisDiscretoModel
from eventoMacro.models import EventoMacroModel
from .serializers import ParamDiscrFisiSerializer
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

from criterioAlerta.views import getUmbralDR as getUmbralDR
from criterioAlerta.views import getUmbralML as getUmbralML
from alertas.models import AlertasModel
from django.db.models import Max

def getAll():
    parametro = ParmFisDiscretoModel.objects.all()[:10000]
    serializer = ParamDiscrFisiSerializer(parametro, many=True)
    #return Response(serializer.data, status=status.HTTP_200_OK)
    return serializer.data

def getParametrosEntreFechas(t1,t2):
    fechaActual=datetime.now()
    fecha1=fechaActual.strftime("%Y-%m-%d %H:%M:%S")
    fecha2=(fechaActual-timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
    parametros=ParmFisDiscretoModel.objects.filter(tiempo__range=(t1,t2))
    serializer = ParamDiscrFisiSerializer(parametros, many=True)
    return serializer.data




def recorrerParametros():
    
    parametros = getAll()
    for  parametro in parametros:
        criterioDr=getUmbralDR(parametro["evento_macro"]["volcan_id"])
        criterioMl=getUmbralML(parametro["evento_macro"]["volcan_id"])
        if(parametro["ml"]>=criterioMl or parametro["dr_c"]>=criterioDr):
            eventoMacro=getEventoMacroId(parametro["evento_macro"]["evento_macro_id"])  
            alerta= AlertasModel(evento=eventoMacro)
            alerta.save()
    # for parametro in parametros:
      
    #for parametro in parametros:
    #    evento_macro_id = parametro.evento_macro_id
    #    print(evento_macro_id)
@api_view(['GET'])
def getMaxDr(request):
    serializer_context = {
        'request': Request(request),
    }
    drMax = ParmFisDiscretoModel.objects.aggregate(Max('dr_c'))
    return Response(drMax, status=status.HTTP_200_OK)

@api_view(['GET'])
def index(request):
    serializer_context = {
        'request': Request(request),
    }
    parametro = ParmFisDiscretoModel.objects.all()[:100]
    serializer = ParamDiscrFisiSerializer(parametro, many=True)
    # return Response(serializer.data, status=status.HTTP_200_OK)
    qs_json = serializers.serialize('json', parametro)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    evento = EventoMacroModel.objects.get(macro_event_id=request.data['macro_event_id'])
    serializer = ParamDiscrFisiSerializer(data=request.data)
    if serializer.is_valid():
        # print(serializer.data)
        serializer.save(volcan=vol)
        return getAll()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update(request, id):
    try:
        criterioAux = ParmFisDiscretoModel.objects.get(criterio_id=id)
        serializer = ParamDiscrFisiSerializer(data=request.data, instance=criterioAux)
        if serializer.is_valid():
            serializer.save()
            return getAll()
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def destroy(request, id):
    try:
        criterio = ParmFisDiscretoModel.objects.get(criterio_id=id)
        criterio.delete()
        return getAll()
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)

