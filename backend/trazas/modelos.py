# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlgoritmoClasifiacion(models.Model):
    id_algoritmo_clasi = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algoritmo_clasifiacion'


class AlgoritmoPicking(models.Model):
    id_algoritmo_picking = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=140)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algoritmo_picking'


class AlgortimoDeteccion(models.Model):
    id_algortimo_deteccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algortimo_deteccion'


class AvistamientoRegistro(models.Model):
    cod_event = models.OneToOneField('IndentificacionSenal', models.DO_NOTHING, db_column='cod_event', primary_key=True)
    cod_event_in = models.CharField(max_length=20)
    id_evento_macro = models.ForeignKey('EventoMacro', models.DO_NOTHING, db_column='id_evento_macro')
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
    componente = models.CharField(max_length=1)
    snr = models.FloatField()
    id_tecnica = models.ForeignKey(AlgoritmoPicking, models.DO_NOTHING, db_column='id_tecnica')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avistamiento_registro'


class Estacion(models.Model):
    id_estacion = models.CharField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=45)
    sensor = models.CharField(max_length=45, blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    latitud = models.CharField(max_length=45)
    longitud = models.CharField(max_length=45)
    altura = models.CharField(max_length=45)
    volcan = models.ForeignKey('Volcan', models.DO_NOTHING, db_column='volcan')
    distancia_crater = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estacion'


class EventoLocalizado(models.Model):
    id_evento_loc = models.BigAutoField(primary_key=True)
    id_evento_macro = models.ForeignKey('EventoMacro', models.DO_NOTHING, db_column='id_evento_macro')
    tiempo = models.DateTimeField()
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
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_localizado'


class EventoMacro(models.Model):
    id_evento_macro = models.BigAutoField(primary_key=True)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_macro'


class IndentificacionSenal(models.Model):
    cod_event = models.BigAutoField(primary_key=True)
    cod_event_in = models.CharField(max_length=20)
    volcan = models.CharField(max_length=12)
    est = models.ForeignKey(Estacion, models.DO_NOTHING, db_column='est')
    componente = models.CharField(max_length=1)
    id_cl = models.ForeignKey(AlgoritmoClasifiacion, models.DO_NOTHING, db_column='id_cl')
    id_det = models.ForeignKey(AlgortimoDeteccion, models.DO_NOTHING, db_column='id_det')
    fecha_pick = models.CharField(max_length=30)
    analista = models.CharField(max_length=45)
    snr = models.FloatField(blank=True, null=True)
    label_event = models.CharField(max_length=45, blank=True, null=True)
    c_label = models.IntegerField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    prom_ruido_fondo = models.FloatField(blank=True, null=True)
    inicio = models.FloatField()
    fin = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    indentificacion_senalcol = models.CharField(db_column='Indentificacion_Senalcol', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'indentificacion_senal'


class Volcan(models.Model):
    id_volcan = models.CharField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    latitud = models.CharField(max_length=45, blank=True, null=True)
    longitud = models.CharField(max_length=45)
    altura = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volcan'
