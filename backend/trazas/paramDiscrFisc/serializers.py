from rest_framework import serializers

from .models import ParmFisDiscretoModel
from eventoMacro.serializers import EventoMacroSerializer

class ParamDiscrFisiSerializer(serializers.ModelSerializer):
    evento_macro = EventoMacroSerializer(read_only=True)
    class Meta:
        model = ParmFisDiscretoModel
        fields = ('parm_discr_fisc_id','fecha', 'evento_macro', 'ml', 'dr_c', 'dr_s', 'energia', 'freq', 'created_at', 'updated_at')
