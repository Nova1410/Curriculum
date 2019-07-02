from django import forms
from src.parametros.models import TipoDocu,EstaCivil,Etnia,Cargo,TipoEstu,TipoLogr
from .models import Habilidad,DatosUsua,Experiencia,Educacion,Logro
from .choices import NivelHabilidad,GENEROS
from django.forms import formset_factory, modelformset_factory,inlineformset_factory
from django.contrib.auth.models import User
from src.usuarios.models import Perfil

#Creamos los formularios para cada uno de nuestros modelos

#Formulario para los datos del usuario
class DatosPersonaForm(forms.ModelForm):
    IdTipoDocu = forms.ModelChoiceField(label="Tipo de documento",queryset=TipoDocu.objects.all(),empty_label=None,required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdUsuarios = forms.CharField(label="Numero de documento",widget=forms.HiddenInput(attrs={'class':'form-control'}),required=True)
    Genero = forms.ChoiceField(choices=GENEROS,label="Genero",required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdEtnias = forms.ModelChoiceField(label="Etnia",queryset=Etnia.objects.all(),empty_label=None,required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdEstaCivil = forms.ModelChoiceField(label="Estado civil",queryset=EstaCivil.objects.all(),empty_label=None,required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdPaises = forms.CharField(label="País",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    IdDepartamentos = forms.CharField(label="Departamento",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    IdCiudades = forms.CharField(label="Ciudad",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    Direccion = forms.CharField(label="Dirección",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    Telefono = forms.CharField(label="Teléfono",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    PerfilPro = forms.CharField(label="Perfil",required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':'6','cols':'150'}))
    class Meta:
        model = DatosUsua
        fields = ('IdTipoDocu','IdUsuarios','Genero','IdEtnias','IdEstaCivil','IdPaises','IdDepartamentos','IdCiudades','Direccion','Telefono','PerfilPro')

#Formulario para las experiencias del usuario
class ExperienciaForm(forms.ModelForm):
    IdUsuarios = forms.CharField(label="Numero de documento",widget=forms.HiddenInput(attrs={'class':'form-control'}),)
    IdCargos = forms.ModelChoiceField(label="Cargo", queryset=Cargo.objects.all(),empty_label="Seleccione el cargo",required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdPaises = forms.CharField(label="Numero del paises", widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdDepartamentos = forms.CharField(label="Numero del departamento", widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdCiudades = forms.CharField(label="Numero de ciudad", widget=forms.TextInput(attrs={'class':'form-control'}),)
    Empresa = forms.CharField(label="Nombre de la empresa", widget=forms.TextInput(attrs={'class':'form-control'}),)
    FechaIni = forms.DateField(label="Fecha inicial", widget=forms.DateInput(attrs={'class':'form-control'}),)
    FechaFin = forms.DateField(label="Fecha inicial", widget=forms.DateInput(attrs={'class':'form-control'}),)
    Funciones = forms.CharField(label="Nombre de la funcion", widget=forms.TextInput(attrs={'class':'form-control'}),)
    Logros = forms.CharField(label="Nombre del logro", widget=forms.TextInput(attrs={'class':'form-control'}),)
    class Meta:
        model = Experiencia
        fields = ('IdUsuarios','IdCargos','IdPaises','IdDepartamentos','IdCiudades','Empresa','FechaIni','FechaFin','Funciones','Logros')

#Creamos un formset para poder administrar cada una de las experiencias que tenga el usuario
ExperienciaFormSet = modelformset_factory(Experiencia,form=ExperienciaForm,extra=0,can_delete=True)


#Formulario para las educaciones del usuario
class EducacionForm(forms.ModelForm):
    IdTipoEstu = forms.ModelChoiceField(label="TipoEstu", queryset=TipoEstu.objects.all(),empty_label="Seleccione el tipo de educación",required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    IdUsuarios = forms.CharField(label="Usuario",widget=forms.HiddenInput(attrs={'class':'form-control'}),)
    IdPaises = forms.CharField(label="Pais",widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdDepartamentos = forms.CharField(label="Departamento",widget=forms.TextInput(attrs={'class':'form-control'}),)
    IdCiudades = forms.CharField(label="Ciudad",widget=forms.TextInput(attrs={'class':'form-control'}),)
    Instituto = forms.CharField(label="Institución",widget=forms.TextInput(attrs={'class':'form-control'}),)
    Titulo = forms.CharField(label="Titulo",widget=forms.TextInput(attrs={'class':'form-control'}),)
    FechGrado = forms.DateField(label="Fecha grado", widget=forms.DateInput(attrs={'class':'form-control'}),)
    class Meta:
        model = Educacion
        fields = ('IdTipoEstu','IdUsuarios','IdPaises','IdDepartamentos','IdCiudades','Instituto','Titulo','FechGrado')

#Creamos un formset para poder administrar cada una de las educaciones que tenga el usuario
EducacionesFormSet = modelformset_factory(Educacion,form=EducacionForm,extra=0,can_delete=True)

#Formulario para las habilidades del usuario
class HabilidadForm(forms.ModelForm):
    IdUsuarios = forms.CharField(label="Usuario",widget=forms.HiddenInput(attrs={'class':'form-control'}),)
    NombHabil = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'class':'form-control'}),)
    NiveHabil = forms.ChoiceField(choices=NivelHabilidad,label="Nivel",required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    class Meta:
        model = Habilidad
        fields = ('IdUsuarios', 'NombHabil' ,'NiveHabil')

#Creamos un formset para poder administrar cada una de las habilidades que tenga el usuario
HabilidadFormSet = modelformset_factory(Habilidad,form=HabilidadForm,extra=0,can_delete=True)

class LogrosForm(forms.ModelForm):
    IdUsuarios = forms.CharField(label="Usuario", widget=forms.HiddenInput(attrs={'class':'form-control'}),)
    idTipoLogr = forms.ModelChoiceField(label="TipoLogr", queryset=TipoLogr.objects.all(),empty_label="Seleccione el tipo de logro",required=True,widget=forms.Select(attrs={'class':'form-control'}),)
    FechLogr = forms.DateField(label="Fecha Logro", widget=forms.DateInput(attrs={'class':'form-control'}),)
    NombrLogr = forms.CharField(label="Nombre del Logro",widget=forms.TextInput(attrs={'class':'form-control'}),)
    DescLogr = forms.CharField(label="Desc",required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':'6','cols':'150'}))
    class Meta:
        model = Logro
        fields =  ('idTipoLogr','IdUsuarios','FechLogr','NombrLogr','DescLogr')
LogrosFormSet = modelformset_factory(Logro, form=LogrosForm,extra=0,can_delete=True)

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombres",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Apellidos",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PerfilForm(forms.ModelForm):
    Titulo = forms.CharField(label="Titulo",widget=forms.TextInput(attrs={'class':'form-control'}))
    Ocup = forms.CharField(label="Ocupacion",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Perfil
        fields = ('Titulo', 'Ocup')

