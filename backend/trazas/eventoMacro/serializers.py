from rest_framework import serializers
from .models import EventoMacroModel


class EventoMacroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoMacroModel
        fields = ('evento_macro_id', 'volcan_id', 'clasificacion', 'inicio', 'fin', 'created_at', 'updated_at')