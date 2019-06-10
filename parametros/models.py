from django.db import models
# Create your models here.
class Etnia(models.Model):
    NombEtni = models.CharField(max_length = 50)
    class Meta():
        verbose_name="Etnia"
        verbose_name_plural = "Etnias"
    
    def __str__(self):
        return self.NombEtni

class TipoDocu(models.Model):
    NombTiDo = models.CharField(max_length = 50)
    class Meta():
        verbose_name="TipoDocumento"
        verbose_name_plural = "TipoDocumentos"
    
    def __str__(self):
        return self.NombTiDo

class EstaCivil(models.Model):
    NombEsCi = models.CharField(max_length = 50)
    class Meta():
        verbose_name="EstadoCivil"
        verbose_name_plural = "EstadosCiviles"
    
    def __str__(self):
        return self.NombEsCi

class TipoEstu(models.Model):
    NombTiEs = models.CharField(max_length = 50)
    class Meta():
        verbose_name="TipoEstudio"
        verbose_name_plural = "TipoEstudios"
    
    def __str__(self):
        return self.NombTiEs

class TipoLogr(models.Model):
    NombTiLo = models.CharField(max_length = 50)

    class Meta():
        verbose_name="TipoLogro"
        verbose_name_plural = "TipoLogros"
    def __str__(self):
        return self.NombTiLo
    
class Cargos(models.Model):
    DomiCargo = models.CharField(max_length = 1, default = "", verbose_name = "DOMINIO")
    ClasCargo = models.CharField(max_length = 2, default = "", verbose_name = "CLASE")
    OrdeCargo = models.CharField(max_length = 3, default = "", verbose_name = "ORDEN")
    GeneCargo = models.CharField(max_length = 4, default = "", verbose_name = "GENERO")
    NomCargo = models.CharField(max_length = 250, default = "", verbose_name = "NOMBRE")
    EsCargo = models.CharField(max_length = 20, default = "", verbose_name = "ES CARGO")

    class Meta():
        verbose_name="Cargos"
        verbose_name_plural = "Empleos y Cargos"
    def __str__(self):
        return self.NomCargo

class Logros (models.Model):
    idLogros = models.IntegerField(verbose_name = "idLogros")
    idTipoLogr = models.ForeignKey(TipoLogr, on_delete = models.CASCADE,verbose_name = "idTipoLogro")
    idTipoUsua = models.IntegerField()
    FechLogr = models.DateField(auto_now=False, verbose_name = "Fecha")
    NombrLogr = models.CharField(max_length = 255, default = "", verbose_name = "Nombre")
    DescLogr = models.TextField(verbose_name = "Descripcion")

    class Meta():
        verbose_name = "Logro"
        verbose_name_plural = "Logros"
    def __str__(self):
        return self.NombrLogr