from rest_framework import serializers
from .models import EventoLocalizadoModel
#from eventoMacro.serializers import EventoMacroSerializer


class EventoLocaliSerializer(serializers.ModelSerializer):
    #evento_macro_id = EventoMacroSerializer(read_only=True)
    class Meta:
        model = EventoLocalizadoModel
        fields = ('evento_loc_id', 'evento_macro_id', 'tiempo', 'lat', 'lon', 'z', 'rmse', 'major_half_axes', 'minor_half_axes', 'dz', 'gap', 'ml', 'n_fases', 'descrip', 'autor', 'created_at', 'updated_at')


class EventoLocaliSerializer2(serializers.ModelSerializer):
    class Meta:
        model = EventoLocalizadoModel
        fields = ('evento_macro_id', 'ml')
        
class EventoLocaliSerializer3(serializers.ModelSerializer):
    class Meta:
        model = EventoLocalizadoModel
        fields = ('evento_macro_id', 'ml','lat','lon')

class EventoLocaliSerializer4(serializers.ModelSerializer):
    class Meta:
        model = EventoLocalizadoModel
        fields = ('evento_macro_id', 'ml','lat','lon')