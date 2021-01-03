from django.db import models

from django.utils.timezone import now

# Create your models here.
class VolcanModel(models.Model):
    id_volcan = models.CharField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    latitud = models.CharField(max_length=45, blank=True, null=True)
    longitud = models.CharField(max_length=45)
    altura = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'volcan'