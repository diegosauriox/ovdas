from django.db import models

# Create your models here.
class AlgoritmoClasifiacionModel(models.Model):
    id_algoritmo_clasi = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'algoritmo_clasifiacion'