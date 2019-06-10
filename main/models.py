from django.db import models

# Create your models here.

class Experiencia(models.Model):
    IdExperiencia = models.IntegerField(verbose_name = "EXPERIENCIA")
    IdUsuarios = models.IntegerField(verbose_name = "USUARIOS")
    IdTipoUsua = models.IntegerField (verbose_name = "TIPOUSUARIO")
    IdCargos = models.IntegerField (verbose_name = "CARGOS")
    IdTipoCarg = models.IntegerField (verbose_name = "TIPOCARGO")
    IdCiudades = models.IntegerField(verbose_name = "CIUDADES")
    IdDepartamentos = models.IntegerField (verbose_name = "DEPARTAMENTOS")
    IdPaises = models.IntegerField (verbose_name = "PAISES")
    Empresas = models.CharField(max_length = 250, default = "", verbose_name = "EMPRESA")
    FechaIni = models.DateTimeField(auto_now=True, verbose_name = "FECHAINICIO")
    FechaFin = models.DateTimeField( auto_noe=True, verbose_name = "FECHAFINAL")
    Funciones = models.CharField(max_length = 500, default = "", verbose_name = "FUNCION")
    Logros = models.CharField(max_length = 500, default = "", verbose_name = "LOGRO")

