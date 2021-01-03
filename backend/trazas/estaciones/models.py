from django.db import models
from volcan.models import VolcanModel

class EstacionModel(models.Model):
    id_estacion = models.CharField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=45)
    sensor = models.CharField(max_length=45, blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    latitud = models.CharField(max_length=45)
    longitud = models.CharField(max_length=45)
    altura = models.CharField(max_length=45)
    volcan = models.ForeignKey(VolcanModel, on_delete=models.CASCADE)
    distancia_crater = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'estacion'