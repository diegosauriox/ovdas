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
