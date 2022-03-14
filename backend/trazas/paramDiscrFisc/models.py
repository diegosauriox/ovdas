from django.db import models
from eventoMacro.models import EventoMacroModel

# Create your models here.
class ParmFisDiscretoModel(models.Model):
    parm_discr_fisc_id = models.IntegerField(primary_key=True)
    fecha = models.CharField(max_length=45)
    evento_macro = models.ForeignKey(EventoMacroModel, models.DO_NOTHING, db_column='evento_macro_id')
    ml = models.FloatField(unique=True, blank=True, null=True)
    dr_c = models.FloatField(blank=True, null=True)
    dr_s = models.FloatField(blank=True, null=True)
    energia = models.FloatField()
    freq = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parm_fis_discreto'
