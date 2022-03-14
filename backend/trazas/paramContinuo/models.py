from django.db import models
from eventoMacro.models import EventoMacroModel
from estaciones.models import EstacionModel

class ParmFisContinuoModel(models.Model):
    fecha = models.CharField(max_length=45, blank=True, null=True)
    est = models.ForeignKey(EstacionModel, on_delete=models.CASCADE)
    rsam = models.FloatField(blank=True, null=True)
    ssam = models.TextField(blank=True, null=True)
    dr = models.FloatField(blank=True, null=True)
    energia = models.FloatField(blank=True, null=True)
    freq = models.FloatField(blank=True, null=True)
    ssam_power = models.TextField(blank=True, null=True)
    rsam_fast = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'parm_fis_continuo'