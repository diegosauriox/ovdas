from django.db import models

import algoritmoClasi
from estaciones.models import EstacionModel
from algoritmoClasi.models import AlgoritmoClasifiacionModel
from algoritmoDetec.models import AlgortimoDeteccionModel

# Create your models here.
class IdentificacionSenalModel(models.Model):
    cod_event = models.BigAutoField(primary_key=True)
    cod_event_in = models.CharField(max_length=20)
    volcan = models.CharField(max_length=12)
    est = models.ForeignKey(EstacionModel, models.DO_NOTHING, db_column='est')
    componente = models.CharField(max_length=1)
    id_cl = models.ForeignKey(AlgoritmoClasifiacionModel, on_delete=models.CASCADE)
    id_det = models.ForeignKey(AlgortimoDeteccionModel, on_delete=models.CASCADE)
    fecha_pick = models.CharField(max_length=30)
    analista = models.CharField(max_length=45)
    snr = models.FloatField(blank=True, null=True)
    label_event = models.CharField(max_length=45, blank=True, null=True)
    c_label = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    prom_ruido_fondo = models.FloatField(blank=True, null=True)
    inicio = models.FloatField()
    fin = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'identificacion_senal'