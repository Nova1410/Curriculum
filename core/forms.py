from django import forms
from .models import Contacto

class ContactForm(forms.ModelForm):
    email = forms.EmailField(label="Correo electrónico",widget=forms.EmailInput(attrs={'class':'form-control'}),required=True)
    asunto = forms.CharField(label="Asunto",required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    msj = forms.CharField(label="Mensaje",required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':'5','cols':'60'}))

    class Meta:
        model = Contacto
        fields = ('email','asunto','msj',)
