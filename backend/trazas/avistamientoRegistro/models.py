from django.db import models
from algoritmoPick.models import AlgoritmoPickingModel
from apibackend.serializers import EventoMacroSerializer
from eventoMacro.models import EventoMacroModel
from identificacion.models import IdentificacionSenalModel
from identificacion.models import IdentificacionSenalModel

class AvistamientoRegistroModel(models.Model):
    cod_event = models.OneToOneField(IdentificacionSenalModel, on_delete=models.CASCADE, db_column='cod_event', primary_key=True)
    #cod_event_in = models.CharField(max_length=20)
    evento_macro = models.ForeignKey(EventoMacroModel, on_delete=models.CASCADE)
    t_p = models.CharField(max_length=45)
    t_s = models.CharField(max_length=45)
    coda = models.CharField(max_length=45)
    c_p = models.IntegerField()
    c_s = models.IntegerField()
    c_coda = models.IntegerField()
    polar = models.CharField(max_length=2, blank=True, null=True)
    frecuencia = models.FloatField(blank=True, null=True)
    amplitud = models.FloatField(blank=True, null=True)
    autor = models.CharField(max_length=45, blank=True, null=True)
    label_event = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    componente = models.CharField(max_length=1)
    snr = models.FloatField()
    id_tecnica = models.ForeignKey(AlgoritmoPickingModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avistamiento_registro'