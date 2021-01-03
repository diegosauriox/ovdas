from rest_framework import serializers
from .models import VolcanModel

class VolcanSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolcanModel
        fields = ('id_volcan', 'nombre', 'descripcion', 'latitud', 'longitud', 'altura', 'created_at', 'updated_at')