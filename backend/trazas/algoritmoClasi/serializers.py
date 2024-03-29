from rest_framework import serializers
from .models import AlgoritmoClasifiacionModel


class Algoritmo_Clasi_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AlgoritmoClasifiacionModel
        fields = ('algoritmo_clasi_id', 'nombre', 'descripcion', 'created_at', 'updated_at')