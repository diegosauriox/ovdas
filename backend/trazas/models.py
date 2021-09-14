# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlgoritmoClasifiacion(models.Model):
    algoritmo_clasi_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algoritmo_clasifiacion'


class AlgoritmoPicking(models.Model):
    algoritmo_picking_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=140)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algoritmo_picking'


class AlgortimoDeteccion(models.Model):
    algortimo_deteccion_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algortimo_deteccion'


class AvistamientoRegistro(models.Model):
    cod_event = models.OneToOneField('IdentificacionSenal', models.DO_NOTHING, db_column='cod_event', primary_key=True)
    cod_event_in = models.BigIntegerField()
    evento_macro = models.ForeignKey('EventoMacro', models.DO_NOTHING)
    t_p = models.CharField(max_length=45)
    t_s = models.CharField(max_length=45)
    coda = models.CharField(max_length=45)
    c_p = models.IntegerField()
    c_s = models.IntegerField()
    c_coda = models.IntegerField(blank=True, null=True)
    inicio = models.CharField(max_length=45)
    polar = models.CharField(max_length=2, blank=True, null=True)
    frecuencia = models.FloatField(blank=True, null=True)
    amplitud = models.FloatField(blank=True, null=True)
    autor = models.CharField(max_length=45, blank=True, null=True)
    label_event = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    componente = models.CharField(max_length=1)
    snr = models.FloatField()
    tecnica = models.ForeignKey(AlgoritmoPicking, models.DO_NOTHING)
    fecha_pick = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avistamiento_registro'


class Estacion(models.Model):
    estacion_id = models.CharField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=45)
    sensor = models.CharField(max_length=45, blank=True, null=True)
    digitalizador = models.CharField(max_length=45)
    periodo = models.IntegerField(blank=True, null=True)
    latitud = models.CharField(max_length=45)
    longitud = models.CharField(max_length=45)
    altura = models.CharField(max_length=45)
    volcan = models.ForeignKey('Volcan', models.DO_NOTHING)
    distancia_crater = models.FloatField()
    calibracion = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estacion'


class EventoLocalizado(models.Model):
    evento_loc_id = models.BigAutoField(primary_key=True)
    evento_macro = models.ForeignKey('EventoMacro', models.DO_NOTHING)
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
    evento_macro_id = models.CharField(primary_key=True, max_length=25)
    volcan_id = models.CharField(max_length=3)
    clasificacion = models.CharField(max_length=2, blank=True, null=True)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_macro'


class IdentificacionSenal(models.Model):
    cod_event = models.CharField(primary_key=True, max_length=30)
    cod_event_in = models.BigIntegerField()
    volcan = models.CharField(max_length=12)
    est = models.ForeignKey(Estacion, models.DO_NOTHING, db_column='est')
    componente = models.CharField(max_length=1)
    cl = models.ForeignKey(AlgoritmoClasifiacion, models.DO_NOTHING)
    algo_detecion = models.ForeignKey(AlgortimoDeteccion, models.DO_NOTHING)
    fecha_pick = models.CharField(max_length=30)
    analista = models.CharField(max_length=45)
    snr = models.FloatField(blank=True, null=True)
    label_event = models.CharField(max_length=45, blank=True, null=True)
    c_label = models.FloatField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    prom_ruido_fondo = models.FloatField(blank=True, null=True)
    inicio = models.FloatField()
    fin = models.FloatField()
    largo = models.FloatField(blank=True, null=True)
    prob_vt = models.FloatField(blank=True, null=True)
    prob_lp = models.FloatField(blank=True, null=True)
    prob_tr = models.FloatField(blank=True, null=True)
    prob_ot = models.FloatField(blank=True, null=True)
    prob_ge = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'identificacion_senal'


class ParmFisContinuo(models.Model):
    fecha = models.CharField(max_length=45, blank=True, null=True)
    est = models.ForeignKey(Estacion, models.DO_NOTHING, db_column='est', blank=True, null=True)
    rsam = models.FloatField(blank=True, null=True)
    ssam = models.TextField(blank=True, null=True)
    dr = models.FloatField(blank=True, null=True)
    energia = models.FloatField(blank=True, null=True)
    freq = models.FloatField(blank=True, null=True)
    ssam_power = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parm_fis_continuo'


class ParmFisDiscreto(models.Model):
    fecha = models.CharField(max_length=45)
    evento = models.ForeignKey(EventoMacro, models.DO_NOTHING, db_column='evento')
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


class ParmFisDiscretoEst(models.Model):
    fecha = models.CharField(max_length=45, blank=True, null=True)
    estacion = models.CharField(max_length=3)
    ml = models.FloatField(blank=True, null=True)
    dr_c = models.FloatField(blank=True, null=True)
    dr_s = models.FloatField(blank=True, null=True)
    energia = models.TextField(blank=True, null=True)
    freq = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parm_fis_discreto_est'


class Volcan(models.Model):
    volcan_id = models.CharField(primary_key=True, max_length=3)
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
