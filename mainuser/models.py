from django.db import models
from parametros.models import Etnia,TipoDocu,EstaCivil,TipoEstu,TipoLogr,Cargo
from ckeditor.fields import RichTextField
from .generos import GENEROS

# Create your models here.
class DatosUsua(models.Model):
    IdTipoDocu = models.ForeignKey(TipoDocu,on_delete = models.CASCADE,default="",verbose_name = "Tipo de documento")
    IdUsuarios = models.IntegerField(verbose_name="Id usuario")
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
    idLogros = models.IntegerField(verbose_name = "Id Logros")
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
    IdEducacion = models.IntegerField(verbose_name = "Id educación")
    IdTipoEstu = models.ForeignKey(TipoEstu,on_delete = models.CASCADE,default="",verbose_name = "Tipo de educación")
    IdUsuarios = models.IntegerField(verbose_name = "Id usuario")
    IdPaises = models.IntegerField(verbose_name = "País")
    IdDepartamentos = models.IntegerField(verbose_name = "Departamento")
    IdCiudades = models.IntegerField(verbose_name = "Ciudad")
    Instituto = models.CharField(max_length = 255,default="",verbose_name = "Instituto")
    Titulo = models.CharField(max_length = 255,default="",verbose_name = "Titulo")
    FechGrado = models.DateTimeField(verbose_name = "Fecha de grado")

    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educaciones"

    def __str__(self):
        return self.Instituto + " " + self.Titulo

class Habilidad(models.Model):
    IdUsuarios = models.IntegerField(verbose_name = "Id Usuario")
    NombHabil = models.CharField(max_length = 155,default="", verbose_name = "Nombre Habilidad")
    NiveHabil = models.CharField(max_length = 155,default="", verbose_name = "Nivel Habilidad")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
    
    def __str__(self):
        return self.NombHabil

class Experiencia(models.Model):
    IdExperiencia = models.IntegerField(verbose_name = "Id experiencia")
    IdUsuarios = models.IntegerField(verbose_name = "Id usuario")
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

