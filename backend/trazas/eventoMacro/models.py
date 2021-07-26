from django.db import models
from volcan.models import VolcanModel

class EventoMacroModel(models.Model):
    id_evento_macro = models.CharField(max_length=25 ,primary_key=True)
    volcan_id = models.CharField(max_length=3)
    inicio = models.CharField(max_length=45)
    fin = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'evento_macro'
