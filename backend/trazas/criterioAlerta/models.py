from django.db import models
from volcan.models import VolcanModel

# Create your models here.

class CriterioAlertaModel(models.Model):
    criterio_id = models.BigIntegerField(primary_key=True)
    volcan = models.ForeignKey(VolcanModel, on_delete=models.CASCADE)
    cantidad_vt = models.IntegerField()
    cantidad_lp = models.IntegerField()
    umbral_ml = models.FloatField()
    umbral_dr = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'criterio_alerta'