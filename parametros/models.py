from django.db import models

# Create your models here.
class Etnia(models.Model):
    NombEtni = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombEtni

class TipoDocu(models.Model):
    NombTiDo = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombTiDo

class EstaCivil(models.Model):
    NombEsCi = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombEsCi

class TipoEstu(models.Model):
    NombTiEs = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombTiEs

class TipoLogr(models.Model):
    NombTiLo = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombTiLo