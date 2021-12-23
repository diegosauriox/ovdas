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



def getAll():
    parametro = ParmFisDiscretoModel.objects.all()
    serializer = ParamDiscrFisiSerializer(parametro, many=True)
    #return Response(serializer.data, status=status.HTTP_200_OK)
    return serializer.data

@api_view(['GET'])
def recorrerParametros(request):
    serializer_context = {
        'request': Request(request),
    }
    parametros = getAll()
    print(parametros[0]['evento_macro'])
    return Response(parametros,status.HTTP_200_OK)
    #for parametro in parametros:
    #    evento_macro_id = parametro.evento_macro_id
    #    print(evento_macro_id)


@api_view(['GET'])
def index(request):
    serializer_context = {
        'request': Request(request),
    }
    parametro = ParmFisDiscretoModel.objects.all()
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

