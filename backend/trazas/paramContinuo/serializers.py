from rest_framework import serializers

from apibackend.models import VolcanModel
from .models import ParmFisContinuoModel
from estaciones.serializers import EstacionSerializer

class ParamContinuoSerializer(serializers.ModelSerializer):
    est = EstacionSerializer(read_only=True)
    class Meta:
        model = ParmFisContinuoModel
        fields = ('fecha', 'est', 'rsam', 'ssam', 'dr','energia', 'freq', 'ssam_power', 'rsam_fast', 'created_at', 'updated_at')
