from rest_framework import serializers
from .models import AlgoritmoPickingModel


class AlgoritmoPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgoritmoPickingModel
        fields = ('id_algoritmo_picking', 'nombre', 'descripcion', 'created_at', 'updated_at')