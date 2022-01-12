from criterioAlerta.models import CriterioAlertaModel
from volcan.models import VolcanModel
from .serializers import CriterioAlertaSerializer
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers


def getUmbralDR(volcan_id):
    criterio = CriterioAlertaModel.objects.get(volcan_id=volcan_id)
    #datos = {"umbral_vt": criterio.umbral_vt}
    return criterio.umbral_dr
def getUmbralML(volcan_id):
    criterio = CriterioAlertaModel.objects.get(volcan_id=volcan_id)
    #datos = {"umbral_vt": criterio.umbral_vt}
    return criterio.umbral_ml

@api_view(['GET'])
def index(request):
    serializer_context = {
        'request': Request(request),
    }
    criterio = CriterioAlertaModel.objects.all()
    serializer = CriterioAlertaSerializer(criterio, many=True)

    #return Response(serializer.data, status=status.HTTP_200_OK)
    qs_json = serializers.serialize('json', criterio)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    vol = VolcanModel.objects.get(volcan_id=request.data['volcan_id'])
    serializer = CriterioAlertaSerializer(data=request.data)
    if serializer.is_valid():
        #print(serializer.data)
        serializer.save(volcan=vol)
        return getAll()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getAll():
    criterios = CriterioAlertaModel.objects.all()
    serializer = CriterioAlertaSerializer(criterios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update(request, id):
    try:
        criterioAux = CriterioAlertaModel.objects.get(criterio_id=id)
        serializer = CriterioAlertaSerializer(data=request.data, instance =criterioAux)
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
        criterio = CriterioAlertaModel.objects.get(criterio_id=id)
        criterio.delete()
        return getAll()
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)