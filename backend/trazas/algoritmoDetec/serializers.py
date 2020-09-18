from rest_framework import serializers
from .models import AlgortimoDeteccionModel


class Algoritmo_Detec_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AlgortimoDeteccionModel
        fields = ('id_algortimo_deteccion', 'nombre', 'descripcion', 'created_at', 'updated_at')