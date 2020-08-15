from rest_framework import serializers
from .models import EstacionModel

class EstacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EstacionModel
        fields = ('id_estacion', 'nombre', 'sensor', 'periodo', 'latitud', 'longitud', 'altura', 'volcan', 'distancia_crater', 'created_at', 'updated_at')