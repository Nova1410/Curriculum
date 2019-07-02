from django import forms
from .models import Contacto
from django.contrib.auth.models import User
from src.parametros.models import TipoDocu, EstaCivil, Etnia
from src.usuarios.models import Perfil

class MultipleForm(forms.ModelForm):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class ContactForm(MultipleForm):
    email = forms.EmailField(label="Correo electrónico",widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
    asunto = forms.CharField(label="Asunto",required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    msj = forms.CharField(label="Mensaje",required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':'5','cols':'60'}))

    class Meta:
        model = Contacto
        fields = ('email','asunto','msj',)

class UserForm(forms.ModelForm):
    username = forms.CharField(label="Usuario",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
    first_name = forms.CharField(label="Nombres",widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Apellidos",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class PerfilForm(forms.ModelForm):
    IdTipoDocu = forms.ModelChoiceField(label="Tipo de documento",queryset=TipoDocu.objects.all(),empty_label="Seleccione el tipo de documento",widget=forms.Select(attrs={'class':'form-control'}))
    #IdEtnia = forms.ModelChoiceField(label="Etnia",queryset=Etnia.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    #IdEstaCivil = forms.ModelChoiceField(label="Estado Civil",queryset=EstaCivil.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    IdUsuarios = forms.CharField(label="Numero de documento",widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    Titulo = forms.CharField(label="Titulo",widget=forms.TextInput(attrs={'class':'form-control'}))
    Ocup = forms.CharField(label="Ocupacion",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Perfil
        fields = ('IdUsuarios', 'Titulo', 'Ocup')

