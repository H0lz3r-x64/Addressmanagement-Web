# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    prv_fir = models.CharField(db_column='PRV_FIR', max_length=6)  # Field name made lowercase.
    fam_name = models.CharField(db_column='FAM_NAME', max_length=40)  # Field name made lowercase.
    vor_namen = models.CharField(db_column='VOR_NAMEN', max_length=40)  # Field name made lowercase.
    titel_1 = models.CharField(db_column='TITEL_1', max_length=10)  # Field name made lowercase.
    titel_2 = models.CharField(db_column='TITEL_2', max_length=10)  # Field name made lowercase.
    titel_3 = models.CharField(db_column='TITEL_3', max_length=10)  # Field name made lowercase.
    geb_datum = models.CharField(db_column='GEB_DATUM', max_length=10)  # Field name made lowercase.
    str = models.CharField(db_column='STR', max_length=40)  # Field name made lowercase.
    str_nr = models.CharField(db_column='STR_NR', max_length=10)  # Field name made lowercase.
    ort = models.CharField(db_column='ORT', max_length=40)  # Field name made lowercase.
    plz = models.IntegerField(db_column='PLZ')  # Field name made lowercase.
    land = models.CharField(db_column='LAND', max_length=40)  # Field name made lowercase.
    lkz = models.CharField(db_column='LKZ', max_length=5)  # Field name made lowercase.
    gesch_mail = models.CharField(db_column='GESCH_MAIL', max_length=40)  # Field name made lowercase.
    gesch_nr = models.CharField(db_column='GESCH_NR', max_length=40)  # Field name made lowercase.
    mobil_nr = models.CharField(db_column='MOBIL_NR', max_length=40)  # Field name made lowercase.
    anz_kinder = models.IntegerField(db_column='ANZ_KINDER')  # Field name made lowercase.
    portrait = models.CharField(db_column='PORTRAIT', max_length=100)  # Field name made lowercase.
    last_edited = models.CharField(db_column='LAST_EDITED', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'addresses'

    def publish(self):
        self.save()

    def __str__(self):
        attrs = vars(Addresses)
        out = (', '.join("%s: %s" % item for item in attrs.items()))
        return out
