from rest_framework import serializers

from apibackend.models import VolcanModel
from .models import EstacionModel
from volcan.serializers import VolcanSerializer

class EstacionSerializer(serializers.ModelSerializer):
    volcan = VolcanSerializer(read_only=True)
    class Meta:
        model = EstacionModel
        fields = ('estacion_id', 'nombre', 'sensor', 'prioridad', 'digitalizador','periodo', 'latitud', 'longitud', 'volcan', 'distancia_crater', 'calibracion', 'poles', 'zeros', 'gain', 'created_at', 'updated_at')
