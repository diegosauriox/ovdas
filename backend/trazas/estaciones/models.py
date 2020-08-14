from django.db import models

class EstacionModel(models.Model):
    id_estacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    sensor = models.CharField(max_length=45, blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    latitud = models.CharField(max_length=45)
    longitud = models.CharField(max_length=45)
    altura = models.CharField(max_length=45)
    volcan = models.IntegerField()
    distancia_crater = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'estacion'