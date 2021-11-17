from django.db import models

# Create your models here.

class AlertasModel(model.Model):
    alerta_id = models.CharField(max_length=25 ,primary_key=True)
    evento_id = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'alerta'