from rest_framework import serializers
from .models import VolcanModel

class VolcanSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolcanModel
        fields = ('volcan_id', 'nombre', 'descripcion', 'latitud', 'longitud', 'altura', 'created_at', 'updated_at')