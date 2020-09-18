from rest_framework import serializers
from .models import EventoMacroModel


class EventoMacroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoMacroModel
        fields = ('id_evento_macro', 'volcan_id', 'inicio', 'fin', 'created_at', 'updated_at')