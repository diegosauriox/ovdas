from rest_framework import serializers

from .models import AlertasModel


class AlertasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertasModel
        fields = ('alerta_id', 'evento_id', 'created_at', 'updated_at', 'evento_macro.volcan_id')

class AlertasSerializer2(serializers.ModelSerializer):
    class Meta:
        model = AlertasModel
        fields = ('alerta_id', 'evento_id','motivo', 'created_at', 'updated_at')