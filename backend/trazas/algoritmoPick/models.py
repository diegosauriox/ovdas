from django.db import models

class AlgoritmoPickingModel(models.Model):
    id_algoritmo_picking = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=140)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algoritmo_picking'