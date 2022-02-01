from django.db import models
from eventoMacro.models import EventoMacroModel

# Create your models here.

class AlertasModel(models.Model):
    alerta_id = models.BigIntegerField(max_length=45, primary_key=True)
    evento = models.ForeignKey(EventoMacroModel, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'alerta'