from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ParmFisContinuoModel
from .serializers import ParamContinuoSerializer
from datetime import datetime

@api_view(['GET'])
def getRsamActual(request):
    mesActual = datetime.now()
    # conteo de eventos simple

    rsam = ParmFisContinuoModel.objects.values('created_at', 'rsam', 'freq', 'energia', 'dr').filter(created_at__month=mesActual.month, rsam__range=(0, 3))
    print(rsam)
    serializer = ParamContinuoSerializer(rsam, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)