from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .multiforms import MultiFormsView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from src.usuarios.models import Perfil
from src.mainuser.models import DatosUsua
from src.parametros.models import TipoDocu,EstaCivil,Etnia,TipoEstu,TipoLogr,Cargo

from django.urls import reverse

from .forms import ContactForm, UserForm, PerfilForm
from .models import Contacto

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in


# Create your views here.

class CoreMultipleFormsView(MultiFormsView):
    template_name = "index.html"
    form_classes = {'contact': ContactForm,
                    'login': AuthenticationForm
                    }

    success_urls = {
        'contact': '/?OK',
    }

    def contact_form_valid(self, form):
        form_name = form.cleaned_data.get('action')
        #Retornamos los valores de los campos
        email = self.request.POST.get('email','')
        asunto = self.request.POST.get('asunto','')
        msj = self.request.POST.get('msj','')
        #Si todo sale bien, guardamos y redireccionamos al nombre de la url con un mensaje
        form.save()
        return HttpResponseRedirect(self.get_success_url(form_name))
    
    def login_form_valid(self, form):
        success_url =  reverse_lazy("usuario:inicio")
        if form.get_user() is not None:
            login(self.request, form.get_user())
            return HttpResponseRedirect(success_url)
        #else:
            # Return an 'invalid login' error message.
        


#def indexcore(request):
    #Instanciamos el formulario de contacto
    #FormContact = ContactForm()
    #Validamos que se haya hecho la petición post del formulario de contacto
    #if request.method == "POST":
        #Reasignamos el valor de FormContact, esta vez con todos los datos del formulario
     #   FormContact = ContactForm(data=request.POST)
        #Validaremos que todos los campos son del tipo de dato correcto
      #  if FormContact.is_valid():

            #Retornamos los valores de los campos
       #     email = request.POST.get('email','')
        #    asunto = request.POST.get('asunto','')
         #   msj = request.POST.get('msj','')
            #Si todo sale bien, guardamos y redireccionamos al nombre de la url con un mensaje
          #  FormContact.save()
            #return redirect(reverse('inicio')+"?OK")
            #Otra forma de redireccionar
           # return redirect('/?OK')
    # Después de instanciado lo pasamos en un diccionario de contexto
    #return render(request, 'index.html',{'formulario':FormContact})

@receiver(user_logged_in)
def sig_user_logged_in(sender,user,request,**kwargs):
        request.session['isLoggedIn'] = True
        request.session['isAdmin'] = user.is_superuser
        request.session['idUserP'] = user.perfil.IdUsuarios
        request.session['idUser'] = user.id

def nosotros(request):
        return render(request,'nosotros.html')


def registro(request):
    if request.method == 'POST':
        userRegistro = UserForm(request.POST)
        perfilRegistro = PerfilForm(request.POST)
        if userRegistro.is_valid() and perfilRegistro.is_valid():
            
            #Se traen los datos del formulario para crear el usuario
            NombUsua = request.POST.get('username', '')
            Email = request.POST.get('email', '')
            Nombres = request.POST.get('first_name', '')
            Apellidos = request.POST.get('last_name', '')
            Contrasena = request.POST.get('password', '')
            #Se crea el usuario pasándole los datos del formulario
            user = User.objects.create_user(username=NombUsua, password=Contrasena, first_name=Nombres, last_name=Apellidos, email=Email)
            
            #Se trae el dato de tipo de documento y se crea un objeto a partir del valor que escogió el usuario
            IdTipoDocu = request.POST.get('IdTipoDocu','')

            #Se crea un objeto default de las foráneas necesarias
            tipodocu = get_object_or_404(TipoDocu,id=IdTipoDocu)
            idetnia = get_object_or_404(Etnia,id=1)
            idestacivil = get_object_or_404(EstaCivil,id=1)
            genero = "Seleccione su genero"

            #Datos del formulario del perfil
            IdUsuarios = request.POST.get('IdUsuarios','')
            Titulo = request.POST.get('Titulo', '')
            Ocup = request.POST.get('Ocup', '')
            
            #Se crean todos los datos del usuario por defecto
            Perfil.objects.create(user=user, IdUsuarios=IdUsuarios, Titulo=Titulo, Ocup=Ocup)
            DatosUsua.objects.create(IdTipoDocu=tipodocu,IdUsuarios=IdUsuarios, IdEstaCivil=idestacivil, IdEtnias=idetnia,IdPaises=0,IdDepartamentos=0,IdCiudades=0,foto="",PerfilPro="",Genero=genero,Telefono="",Direccion="")
            return redirect('/?OK')
    else:
        userRegistro = UserForm()
        perfilRegistro = PerfilForm()
    return render(request,'registro.html', {'formUser':userRegistro, 'formPerfil':perfilRegistro})


