# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser 

class Auser(AbstractUser):
    phone_num = models.IntegerField(blank = False, null = True)

    class Meta:
        # managed = False
        db_table = 'auser'

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    phone_num = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    user = models.ForeignKey(Auser, on_delete = models.CASCADE, null = True)

    class Meta:
        # managed = False
        db_table = 'patient'


class Herb(models.Model):
    herb_id = models.AutoField(primary_key=True)
    herb_name = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'herb'


class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    description = models.CharField(max_length=500, blank=True, null=True)
    record_date = models.DateField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'record'
        unique_together = (('record_id', 'patient'),)

class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    herb = models.ForeignKey(Herb, on_delete=models.SET_NULL, null = True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'prescription'
        unique_together = (('prescription_id', 'herb'),)

