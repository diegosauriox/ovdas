from django.db import models
from eventoMacro.models import EventoMacroModel

class EventoLocalizadoModel(models.Model):
    evento_loc_id = models.BigIntegerField(primary_key=True, max_length=45)
    evento_macro = models.ForeignKey(EventoMacroModel, on_delete=models.CASCADE)
    tiempo = models.DateTimeField()
    lat = models.CharField(max_length=45)
    lon = models.CharField(max_length=45)
    z = models.FloatField()
    rmse = models.FloatField()
    major_half_axes = models.FloatField()
    minor_half_axes = models.FloatField()
    dz = models.CharField(max_length=45)
    gap = models.FloatField()
    ml = models.FloatField(blank=True, null=True)
    n_fases = models.IntegerField()
    descrip = models.CharField(max_length=45)
    autor = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_localizado'