from django.db import models

# Create your models here.

class Experiencia(models.Model):
    IdExperiencia = models.IntegerField(verbose_name = "Experiencia")
    IdUsuarios = models.IntegerField(verbose_name = "Usuario")
    IdTipoUsua = models.ForeignKey (TipoUsua, on_delete = models.CASCADE, verbose_name = "Tipo Usuario")
    IdCargos = models.ForeignKey (Cargos, on_delete = models.CASCADE ,verbose_name = "Cargo")
    IdTipoCarg = models.ForeignKey (TipoCarg, on_delete = models.CASCADE ,verbose_name = "Tipo Cargo")
    IdCiudades = models.ForeignKey(Ciudades, on_delete = models.CASCADE ,verbose_name = "Ciudad")
    IdDepartamentos = models.ForeignKey (Departamentos, on_delete = models.CASCADE ,verbose_name = "Departamento")
    IdPaises = models.ForeignKey (Paises, on_delete = models.CASCADE ,verbose_name = "Pais")
    Empresas = models.CharField(max_length = 250, default = "", verbose_name = "EMPRESA")
    FechaIni = models.DateTimeField(auto_now=True, verbose_name = "FECHAINICIO")
    FechaFin = models.DateTimeField( auto_noe=True, verbose_name = "FECHAFINAL")
    Funciones = models.CharField(max_length = 500, default = "", verbose_name = "FUNCION")
    Logros = models.CharField(max_length = 500, default = "", verbose_name = "LOGRO")

