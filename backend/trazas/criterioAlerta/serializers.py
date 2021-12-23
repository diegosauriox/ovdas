from rest_framework import serializers

from apibackend.models import VolcanModel
from .models import CriterioAlertaModel
from volcan.serializers import VolcanSerializer

class CriterioAlertaSerializer(serializers.ModelSerializer):
    volcan = VolcanSerializer(read_only=True)
    class Meta:
        model = CriterioAlertaModel
        fields = ('criterio_id', 'volcan', 'cantidad_vt', 'cantidad_lp', 'umbral_ml', 'umbral_dr', 'created_at', 'updated_at')
