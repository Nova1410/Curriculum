from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .models import DatosUsua,Habilidad,Experiencia,Educacion,Logro
from django.views.generic import CreateView,TemplateView,FormView
from django.urls import reverse_lazy, reverse
from .forms import DatosPersonaForm,ExperienciaForm,HabilidadForm,ExperienciaFormSet,HabilidadFormSet,LogrosFormSet,EducacionesFormSet,UserForm,PerfilForm
from .multiforms import MultiFormsView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from src.usuarios.models import Perfil
from django.contrib.auth.models import User
# Create your views here.

#Clase para mostrar los datos del usuario

class PerfilListView(LoginRequiredMixin,TemplateView):
    #Plantilla donde se mostrarán los datos
    template_name = "perfil.html"
    
    #Función para extraer los datos del usuario logueado
    def get_context_data(self, **kwargs):
        #Miramos cuál es el id del usuario que está logueado
        idUserP = self.request.session.get('idUserP')
        #Asignamos los datos del usuario a unos contextos y los retornamos
        context = super(PerfilListView,self).get_context_data(**kwargs)
        context["datosusuario"] = DatosUsua.objects.filter(IdUsuarios=idUserP)
        context["educaciones"] = Educacion.objects.filter(IdUsuarios=idUserP)
        context["experiencias"] = Experiencia.objects.filter(IdUsuarios = idUserP)
        context["habilidades"] = Habilidad.objects.filter(IdUsuarios=idUserP)
        context["logros"] = Logro.objects.filter(IdUsuarios=idUserP)
        context["perfil"] = Perfil.objects.filter(IdUsuarios=idUserP)
        return context

#Clase para mostrar y utilizar los formularios
class PerfilMultipleFormsView(LoginRequiredMixin,MultiFormsView):
    #Plantilla donde se mostrarán los formularios
    template_name = "perfil_update.html"


    #Llenamos el diccionario de formularios con un nombre y la clase del formulario correspondiente
    form_classes = {'datospersona' : DatosPersonaForm,
                    'experienciasForm': ExperienciaFormSet,
                    'habilidadesForm' : HabilidadFormSet,
                    'logrosForm' : LogrosFormSet,
                    'educacionesForm' : EducacionesFormSet,
                    'usuarioForm' : UserForm,
                    'perfilForm' : PerfilForm
    }

    #Llenamos el diccionario de prefixes asignándole a cada formulario un nombre 
    #para diferenciarlos entre sí
    prefixes = {
        'datospersona' : 'datospersona',
        'experienciasForm' : 'experiencias',
        'habilidadesForm' : 'habilidades',
        'logrosForm' : 'logros',
        'educacionesForm' : 'educaciones',
        'usuarioForm' : 'usuario',
        'perfilForm' : 'perfil'
    }
    
    #Creamos unas variables para controlar los mensajes y alertas que se puedan presentar
    alert = ""
    msj = ""

    idValidator = False

    #Función para validar y procesar los formularios de usuario y perfil
    def user_form_valid(self,request,user,id_perfil):
        if request.method == 'POST':
            #Buscamos el usuario que actualizará sus datos
            inst = get_object_or_404(User,id=int(user))
            #Buscamos el perfil del usuario que actualizará sus datos
            instP = get_object_or_404(Perfil,pk=id_perfil)
            #Instanciamos el usuario y el perfil en sus respectivos formularios
            formUser = UserForm(request.POST,instance=inst,prefix="usuario")
            formPerfil = PerfilForm(request.POST,instance=instP,prefix="perfil")
            
            if formUser.is_valid() and formPerfil.is_valid():

                #Guardamos los formularios de usuario y perfil
                formUser.save()
                formPerfil.save()

                #Creamos el mensaje que se mostrará en la alerta
                self.alert = "alert-success"
                self.msj = "Sus datos han sido actualizados"
                #Mandamos las variables GET que mostrarán el tipo de alerta y el mensaje y redireccionamos
                return HttpResponseRedirect('update?Alert=' + self.alert + '&msj=' + self.msj)
            else:

                #Creamos el mensaje que se mostrará en la alerta de error
                self.alert = "alert-danger"
                self.msj = "Sus datos no han sido actualizados"
                return HttpResponseRedirect('update?Alert=' + self.alert + '&msj=' + self.msj)

    #Función para validar y procesar todos los formularios de la hoja de vida
    def multipleForm_form_valid(self,request,form_IdUser):
        
        if request.method == 'POST':

            validate_userID(self,request,'datospersona',form_IdUser)
            validate_userID(self,request,'experiencias',form_IdUser)
            validate_userID(self,request,'habilidades',form_IdUser)
            validate_userID(self,request,'educaciones',form_IdUser)
            validate_userID(self,request,'logros',form_IdUser)

            if self.idValidator == False:
                #Obtenemos el usuario que va a actualizar o guardar sus datos
                datos = get_object_or_404(DatosUsua,pk=form_IdUser)
                
                
                #Traemos los datos que están en POST de cada formulario y colocamos un prefix
                #a cada formulario para diferenciarlo de otros
                formPersonas = DatosPersonaForm(request.POST,instance=datos,prefix='datospersona')
                formsetExperiencias = ExperienciaFormSet(request.POST,prefix='experiencias')
                formsetHabilidad = HabilidadFormSet(request.POST,prefix='habilidades')
                formsetEducacion = EducacionesFormSet(request.POST,prefix="educaciones")
                formsetLogros = LogrosFormSet(request.POST,prefix='logros')
          
                #Evaluamos si cada formulario es válido, de ser correctos los procesamos y los guardamos
                if formPersonas.is_valid() and formsetExperiencias.is_valid() and formsetHabilidad.is_valid() and formsetEducacion.is_valid() and formsetLogros.is_valid():
                    
                    #Guardamos el formulario de los datos generales
                    formPersonas.save()


                    #Procesamos los formularios que son formsets
                    process_formset(self,formsetExperiencias,request,'experiencias',Experiencia)
                    process_formset(self,formsetHabilidad,request,'habilidades',Habilidad)
                    process_formset(self,formsetLogros,request,'logros',Logro)
                    process_formset(self,formsetEducacion,request,'educaciones',Educacion)
                    #Mandamos las variables GET que mostrarán el tipo de alerta y el mensaje y redireccionamos
                    return HttpResponseRedirect('update?Alert=' + self.alert + '&msj=' + self.msj)
    
                #Si algún formulario es inválido mostraremos una alerta de error 
                #y haremos el respectivo redireccionamiento con sus variables
                else:
                    self.alert = "alert-danger"
                    self.msj = "Sus datos no han sido actualizados"
                    return HttpResponseRedirect('update?Alert=' + self.alert + '&msj=' + self.msj)
            else:
                 return HttpResponseRedirect('update?Alert=' + self.alert + '&msj=' + self.msj)
        
           

#Función para procesar los formset
def process_formset(self,formset,request,prefix,model):
    cont = 0

    #Recorremos cada formulario en el formset
    for form in formset:
        num = str(cont)

        #Buscaremos el id y el botón delete del formulario que entró
        idForm = request.POST.get(prefix + "-" + num + "-id")
        delete = request.POST.get(prefix + "-" + num + "-DELETE")

        #Si el botón delete está seleccionado entonces borraremos esos datos
        if delete == 'on':
            try:
                #Traemos la instancia de los datos que se borrarán
                instance = model.objects.get(pk=idForm)
            #De no existir esos datos mostraremos una alerta de error
            except model.DoesNotExist:
                self.alert = "alert-danger"
                self.msj = "El objeto no ha sido encontrado"
            #Si todo es correcto borraremos los datos
            else:
                instance.delete()
        #Si el botón no está seleccionado entonces guardamos o actualizamos los datos y mostraremos una
        #alerta de que todo fue correcto
        else:
            self.alert = "alert-success"
            self.msj = "Sus datos han sido actualizados"
            form.save()
        cont = cont + 1

def validate_userID(self,request,prefix,form_IdUser):
    if prefix == 'datospersona':
        IdUser = str(request.POST.get(prefix + '-IdUsuarios'))
        if IdUser != str(form_IdUser):
            self.idValidator = True
            self.alert = "alert-danger"
            self.msj = "No puede realizar esa acción"

    else:
        total = int(request.POST.get(prefix + '-TOTAL_FORMS'))
        count = 0
        for i in range(total):
            num = str(count)
            IdUser = str(request.POST.get(prefix + "-" + num + "-IdUsuarios"))
            if(IdUser == ''):
                IdUser = str(form_IdUser)
            if IdUser != str(form_IdUser):
                self.idValidator = True
                self.alert = "alert-danger"
                self.msj = "No puede realizar esa acción"
            count = count + 1
        

#Función para desloguear al usuario
@login_required
def logout_view(request):
        logout(request)
        return HttpResponseRedirect('/')

