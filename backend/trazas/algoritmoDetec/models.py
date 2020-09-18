from django.db import models

# Create your models here.
class AlgortimoDeteccionModel(models.Model):
    id_algortimo_deteccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'algortimo_deteccion'