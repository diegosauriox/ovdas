from rest_framework import serializers
from .models import EventoLocalizadoModel


class EventoLocaliSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoLocalizadoModel
        fields = ('id_evento_loc', 'id_evento_macro	', 'tiempo', 'lat', 'lon', 'z', 'rmse', 'major_half_axes', 'minor_half_axes', 'dz', 'gap', 'ml', 'n_fases', 'descripcion', 'autor', 'created_at', 'updated_at')