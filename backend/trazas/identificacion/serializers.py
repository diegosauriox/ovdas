from rest_framework import serializers
from .models import IdentificacionSenalModel


class IdentificacionSenalSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificacionSenalModel
        fields = ('cod_event', 'cod_event_in', 'volcan', 'est', 'componente', 'id_cl', 'id_det', 'fecha_pick', 'analista', 'snr', 'label_event', 'descripcion', 'inicio', 'fin',  'created_at', 'updated_at')