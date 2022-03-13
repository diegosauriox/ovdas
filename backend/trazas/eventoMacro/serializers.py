from rest_framework import serializers
from .models import EventoMacroModel
from eventoLocali.serializers import EventoLocaliSerializer4
from eventoLocali.models import EventoLocalizadoModel


class EventoMacroSerializer(serializers.ModelSerializer):
    #volcan = VolcanSerializer(read_only=True)
    class Meta:
        model = EventoMacroModel
        fields = ('evento_macro_id', 'volcan_id', 'clasificacion', 'inicio', 'fin', 'probabilidad', 'confiabilidad', 'created_at', 'updated_at')

class EventoMacroSerializer2(serializers.ModelSerializer):
    #localizacion = EventoLocalizadoModel(read_only=True)
    localizacion = EventoLocaliSerializer4(many=True, read_only=True)
    class Meta:
        model = EventoMacroModel
        fields = '__all__ '