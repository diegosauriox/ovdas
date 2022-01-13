from rest_framework import serializers
from .models import AvistamientoRegistroModel


class AvistamientoRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvistamientoRegistroModel
        fields = ('cod_event', 'cod_event_in', 'evento_macro_id','t_p', 't_s', 'coda', 'c_p', 'c_s', 'c_coda', 'inicio','polar', 'frecuencia', 'amplitud', 'autor', 'label_event', 'descripcion', 'componente', 'snr', 'tecnica_id', 'fecha_pick','created_at', 'updated_at')