# serializers.py
from rest_framework import serializers

from .models import *


class FrezHhzTc9920200321Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FrezHhzTc9920200321
        fields = ('st', 'et', 'sr', 'datatype', 'tracebuf')


class EstacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EstacionModel
        fields = ('id_estacion', 'nombre', 'sensor', 'periodo', 'latitud', 'longitud', 'altura', 'volcan', 'distancia_crater', 'create_at', 'update_at')

class EventoMacroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventoMacroModel
        fields = ('id_evento', 'fecha', 'create_at', 'update_at')

class LocalizedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventoLocalizadoModel
        fields = ('id_evento_loc', 'id_evento_macro', 'tiempo', 'lat', 'lon', 'z', 'rmse', 'major, halft_axes', 'minor_half_axes', 'dz', 'gap',  'ml', 'n_fases', 'descrip', 'autor', 'created_at', 'update_at')