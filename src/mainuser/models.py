from django.db import models
from src.parametros.models import Etnia,TipoDocu,EstaCivil,TipoEstu,TipoLogr,Cargo
from ckeditor.fields import RichTextField
from .choices import GENEROS
from .choices import NivelHabilidad

# Creamos nuestros modelos.
class DatosUsua(models.Model):
    IdTipoDocu = models.ForeignKey(TipoDocu,on_delete = models.CASCADE,default="",verbose_name = "Tipo de documento")
    IdUsuarios = models.CharField(max_length = 11,verbose_name="Id usuario",primary_key=True)
    IdEstaCivil = models.ForeignKey(EstaCivil,on_delete = models.CASCADE,default="",verbose_name = "Estado civil")
    IdEtnias = models.ForeignKey(Etnia,on_delete = models.CASCADE,default="",verbose_name = "Etnia")
    IdPaises = models.IntegerField(verbose_name="Pais")
    IdDepartamentos = models.IntegerField(verbose_name="Departamento")
    IdCiudades = models.IntegerField(verbose_name="Ciudad")
    foto = models.FileField(upload_to = "fotos/", max_length = 500,default="foto.jpg",verbose_name = "Foto del usuario")
    PerfilPro = RichTextField(max_length = 200,default="",verbose_name = "Perfil profesional")
    Genero = models.CharField(max_length = 15,choices=GENEROS)
    Telefono = models.CharField(max_length = 50,default="",verbose_name = "Telefono")
    Direccion = models.CharField(max_length = 100,default="",verbose_name = "Direccion")

    class Meta():
        verbose_name = "Datos de usuario"
        verbose_name_plural = "Datos de usuarios"
    def __str__(self):
        return str(self.IdUsuarios)

class Logro(models.Model):
    IdUsuarios = models.CharField(max_length = 11,verbose_name = "Id usuario")
    idTipoLogr = models.ForeignKey(TipoLogr, on_delete = models.CASCADE,default="",verbose_name = "Id tipo de logro")
    FechLogr = models.DateField(auto_now=False,verbose_name = "Fecha")
    NombrLogr = models.CharField(max_length = 255, default = "", verbose_name = "Nombre logro")
    DescLogr = RichTextField(max_length = 200,default="",verbose_name = "Descripcion")

    class Meta():
        verbose_name = "Logro"
        verbose_name_plural = "Logros"
    def __str__(self):
        return self.NombrLogr

class Educacion(models.Model):
    IdTipoEstu = models.ForeignKey(TipoEstu,on_delete = models.CASCADE,default="",verbose_name = "Tipo de educación")
    IdUsuarios = models.CharField(max_length = 11,verbose_name = "Id usuario")
    IdPaises = models.IntegerField(verbose_name = "País")
    IdDepartamentos = models.IntegerField(verbose_name = "Departamento")
    IdCiudades = models.IntegerField(verbose_name = "Ciudad")
    Instituto = models.CharField(max_length = 255,default="",verbose_name = "Instituto")
    Titulo = models.CharField(max_length = 255,default="",verbose_name = "Titulo")
    FechGrado = models.DateField(verbose_name = "Fecha de grado")

    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educaciones"

    def __str__(self):
        return self.Instituto + " " + self.Titulo

class Habilidad(models.Model):
    IdUsuarios = models.CharField(max_length = 11,verbose_name = "Id Usuario")
    NombHabil = models.CharField(max_length = 155,default="", verbose_name = "Nombre Habilidad")
    NiveHabil = models.CharField(max_length = 50,choices=NivelHabilidad,default="", verbose_name = "Nivel Habilidad")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
    
    def __str__(self):
        return self.NombHabil

class Experiencia(models.Model):
    IdUsuarios = models.CharField(max_length = 11,verbose_name = "Id usuario")
    IdCargos = models.ForeignKey(Cargo,on_delete = models.CASCADE,default="",verbose_name = "Cargo")
    IdPaises = models.IntegerField (verbose_name = "Pais")
    IdDepartamentos = models.IntegerField (verbose_name = "Departamento")
    IdCiudades = models.IntegerField(verbose_name = "Ciudad")
    Empresa = models.CharField(max_length = 250, default = "", verbose_name = "Empresa")
    FechaIni = models.DateField(verbose_name = "Fecha de inicio")
    FechaFin = models.DateField(verbose_name = "Fecha de finalizacion")
    Funciones = models.CharField(max_length = 500, default = "", verbose_name = "Funcion")
    Logros = RichTextField(max_length = 500, default = "", verbose_name = "Logros")

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return self.Empresa

