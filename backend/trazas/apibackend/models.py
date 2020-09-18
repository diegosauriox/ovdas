# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class FrezHhzTc9920200321(models.Model):
    st = models.FloatField(primary_key=True)
    et = models.FloatField(blank=True, null=True)
    sr = models.FloatField(blank=True, null=True)
    datatype = models.CharField(max_length=3, blank=True, null=True)
    tracebuf = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frez$hhz$tc$99$$2020_03_21'


class FrezHhzTc9920200322(models.Model):
    st = models.FloatField(primary_key=True)
    et = models.FloatField(blank=True, null=True)
    sr = models.FloatField(blank=True, null=True)
    datatype = models.CharField(max_length=3, blank=True, null=True)
    tracebuf = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frez$hhz$tc$99$$2020_03_22'


class FrezHhzTc9920200323(models.Model):
    st = models.FloatField(primary_key=True)
    et = models.FloatField(blank=True, null=True)
    sr = models.FloatField(blank=True, null=True)
    datatype = models.CharField(max_length=3, blank=True, null=True)
    tracebuf = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frez$hhz$tc$99$$2020_03_23'


class FrezHhzTc9920200324(models.Model):
    st = models.FloatField(primary_key=True)
    et = models.FloatField(blank=True, null=True)
    sr = models.FloatField(blank=True, null=True)
    datatype = models.CharField(max_length=3, blank=True, null=True)
    tracebuf = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frez$hhz$tc$99$$2020_03_24'


class FrezHhzTc99H20200321(models.Model):
    j2ksec = models.FloatField(primary_key=True)
    smin = models.IntegerField(blank=True, null=True)
    smax = models.IntegerField(blank=True, null=True)
    rcnt = models.IntegerField(blank=True, null=True)
    rsam = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frez$hhz$tc$99$$h2020_03_21'


class FrezHhzTc99H20200322(models.Model):
    j2ksec = models.FloatField(primary_key=True)
    smin = models.IntegerField(blank=True, null=True)
    smax = models.IntegerField(blank=True, null=True)
    rcnt = models.IntegerField(blank=True, null=True)
    rsam = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frez$hhz$tc$99$$h2020_03_22'


class FrezHhzTc99H20200323(models.Model):
    j2ksec = models.FloatField(primary_key=True)
    smin = models.IntegerField(blank=True, null=True)
    smax = models.IntegerField(blank=True, null=True)
    rcnt = models.IntegerField(blank=True, null=True)
    rsam = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frez$hhz$tc$99$$h2020_03_23'


class FrezHhzTc99H20200324(models.Model):
    j2ksec = models.FloatField(primary_key=True)
    smin = models.IntegerField(blank=True, null=True)
    smax = models.IntegerField(blank=True, null=True)
    rcnt = models.IntegerField(blank=True, null=True)
    rsam = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frez$hhz$tc$99$$h2020_03_24'

class AlgoritmoClasifiacionModel(models.Model):
    id_algoritmo_clasi = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'algoritmo_clasifiacion'


class AlgortimoDeteccionModel(models.Model):
    id_algortimo_deteccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'algortimo_deteccion'


class AvistamientoRegistroModel(models.Model):
    id_avist_regis = models.BigIntegerField(primary_key=True)
    cod_event = models.CharField(max_length=12)
    t_p = models.CharField(max_length=45)
    t_s = models.CharField(max_length=45)
    coda = models.CharField(max_length=45)
    c_p = models.IntegerField()
    c_s = models.IntegerField()
    c_coda = models.IntegerField()
    polar = models.CharField(max_length=2, blank=True, null=True)
    frecuencia = models.FloatField(blank=True, null=True)
    amplitud = models.FloatField(blank=True, null=True)
    autor = models.CharField(max_length=45, blank=True, null=True)
    lavel_event = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    id_evento_macro = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'avistamiento_registro'


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
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estacion'


class EventoLocalizadoModel(models.Model):
    id_evento_loc = models.BigAutoField(primary_key=True)
    id_evento_macro = models.BigIntegerField()
    tiempo = models.CharField(max_length=19)
    lat = models.CharField(max_length=45)
    lon = models.CharField(max_length=45)
    z = models.FloatField()
    rmse = models.FloatField()
    major_half_axes = models.FloatField()
    minor_half_axes = models.FloatField()
    dz = models.CharField(max_length=45)
    gap = models.FloatField()
    ml = models.FloatField(blank=True, null=True)
    n_fases = models.IntegerField()
    descrip = models.CharField(max_length=45)
    autor = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_localizado'


class EventoMacroModel(models.Model):
    id_evento_macro = models.BigAutoField(primary_key=True)
    fecha = models.DateTimeField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_macro'


class IndentificacionSenalModel(models.Model):
    id_identi_senal = models.BigAutoField(primary_key=True)
    volcan = models.CharField(max_length=12)
    est = models.IntegerField()
    componente = models.CharField(max_length=1)
    code_event = models.CharField(max_length=12)
    id_cl = models.IntegerField()
    id_det = models.PositiveIntegerField()
    fecha_pick = models.DateTimeField()
    analista = models.CharField(max_length=45)
    snr = models.FloatField(blank=True, null=True)
    label_event = models.CharField(max_length=45, blank=True, null=True)
    c_label = models.IntegerField()
    create_at = models.CharField(max_length=45)
    update_at = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    prom_ruido_fondo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indentificacion_senal'


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





