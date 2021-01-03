from rest_framework import serializers
from .models import EstacionModel

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstacionModel
        fields = ('id_estacion', 'nombre', 'sensor', 'periodo', 'latitud', 'longitud', 'volcan_id', 'volcan', 'distancia_crater', 'created_at', 'updated_at')