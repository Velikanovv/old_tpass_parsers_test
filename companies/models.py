# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.utils.translation import gettext_lazy as _



class Company(models.Model):
    name = models.CharField(max_length=1000, default='', blank='COMPANY UNDEF')
    inn = models.CharField(max_length=120, default='', blank='')
    kpp = models.CharField(max_length=10000, default='', blank='')
    ogrn = models.CharField(max_length=10000, default='', blank='')
    fio = models.CharField(max_length=10000, default='', blank='')


class Car(models.Model):
    licence_plate = models.CharField(max_length=50)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.licence_plate


class Pass(models.Model):
    name = models.CharField(max_length=50000)
    ready = models.BooleanField(default=False)

    def __str__(self):
        return self.name

