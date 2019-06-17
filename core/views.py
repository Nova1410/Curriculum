from django.shortcuts import render, HttpResponse,redirect

from django.views.generic.edit import CreateView

from django.urls import reverse

from .forms import ContactForm
from .models import Contacto
# Create your views here.

def indexcore(request):
    #Instanciamos el formulario de contacto
    FormContact = ContactForm()
    #Validamos que se haya hecho la petición post del formulario de contacto
    if request.method == "POST":
        #Reasignamos el valor de FormContact, esta vez con todos los datos del formulario
        FormContact = ContactForm(data=request.POST)
        #Validaremos que todos los campos son del tipo de dato correcto
        if FormContact.is_valid():

            #Retornamos los valores de los campos
            email = request.POST.get('email','')
            asunto = request.POST.get('asunto','')
            msj = request.POST.get('msj','')
            #Si todo sale bien, guardamos y redireccionamos al nombre de la url con un mensaje
            FormContact.save()
            #return redirect(reverse('inicio')+"?OK")
            #Otra forma de redireccionar
            return redirect('/?OK')
    # Después de instanciado lo pasamos en un diccionario de contexto
    return render(request, 'index.html',{'formulario':FormContact})

def nosotros(request):
        return render(request,'nosotros.html')


def registro(request):
        return render(request,'registro.html')


