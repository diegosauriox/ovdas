from rest_framework import serializers
from .models import IdentificacionSenalModel


class IdentificacionSenalSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificacionSenalModel
        fields = ('cod_event', 'cod_event_in', 'volcan', 'est', 'componente', 'algo_detecion_id', 'fecha_pick', 'analista', 'snr', 'label_event', 'c_label', 'descripcion', 'inicio', 'fin', 'prob_ge','created_at', 'updated_at')