from django.db import models

# Create your models here.
class Etnia(models.Model):
    NombEtni = models.CharField(max_length = 50,default = "",verbose_name = "Nombre Etnia")

    def __str__(self):
        return self.NombEtni
    
    class Meta:
        verbose_name = "Etnia"
        verbose_name_plural = "Etnias"

class TipoDocu(models.Model):
    NombTiDo = models.CharField(max_length = 50,default = "",verbose_name = "Nombre tipo de documento")

    def __str__(self):
        return self.NombTiDo
    
    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"

class EstaCivil(models.Model):
    NombEsCi = models.CharField(max_length = 50,default = "",verbose_name = "Nombre estado civil")

    def __str__(self):
        return self.NombEsCi
    
    class Meta:
        verbose_name = "Estado civil"
        verbose_name_plural = "Estados civiles"

class TipoEstu(models.Model):
    NombTiEs = models.CharField(max_length = 50,default = "",verbose_name = "Nombre tipo de educacion")

    def __str__(self):
        return self.NombTiEs
    
    class Meta:
        verbose_name = "Tipos de educacion"
        verbose_name_plural = "Tipos de educaciones"

class TipoLogr(models.Model):
    NombTiLo = models.CharField(max_length = 50,default = "",verbose_name = "Nombre tipo de logro")

    def __str__(self):
        return self.NombTiLo
    
    class Meta:
        verbose_name = "Tipo de logro"
        verbose_name_plural = "Tipos de logros"

class Cargo(models.Model):
    DomiCarg = models.CharField(max_length = 1,default = "", verbose_name = "Dominio") 
    ClasCarg = models.CharField(max_length = 2,default = "", verbose_name = "Clase")
    OrdeCarg = models.CharField(max_length = 3,default = "", verbose_name = "Orden")
    GeneCarg = models.CharField(max_length = 4,default = "", verbose_name = "Genero")
    NombCarg = models.CharField(max_length = 250,default = "", verbose_name = "Nombre")
    EsCargo = models.CharField(max_length = 20,default = "", verbose_name = "Es cargo")

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Empleos y Cargos"

    def __str__(self):
        return self.NombCarg
