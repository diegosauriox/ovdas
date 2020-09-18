from django.db import models
from apibackend.models import VolcanModel

class EventoMacroModel(models.Model):
    id_evento_macro = models.BigAutoField(primary_key=True)
    volcan_id = models.CharField(max_length=3)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_macro'
