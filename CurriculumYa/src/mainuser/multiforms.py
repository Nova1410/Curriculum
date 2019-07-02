from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView
from .models import DatosUsua,Experiencia,Habilidad,Educacion,Logro
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.forms.formsets import formset_factory
from .forms import ExperienciaFormSet, HabilidadFormSet, EducacionesFormSet
from django.contrib.auth.models import User
from src.usuarios.models import Perfil

class MultiFormMixin(ContextMixin):

    #Creamos un diccionario el cual contendrá a cada formulario
    form_classes = {} 

    #Creamos un diccionario el cual contendrá los prefix de cada formulario
    prefixes = {}

    #Creamos un diccionario el cual contendrá las succes_url de cada formulario
    success_urls = {}
    
    initial = {}
    prefix = None
    success_url = None
    
    #Función para obtener las clases de cada formulario
    def get_form_classes(self):
        return self.form_classes
    
    #Función para obtener los formularios
    def get_forms(self, form_classes):
        return dict([(key, self._create_form(key, class_name)) \
            for key, class_name in form_classes.items()])
    
    #Función para obtener los kwargs de cada formulario
    def get_form_kwargs(self, form_name):
        kwargs = {}
        #kwargs.update({'instance': self.get_instance(form_name)})  # helps when updating records
        kwargs.update({'initial':self.get_initial(form_name)})
        kwargs.update({'prefix':self.get_prefix(form_name)})
        
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs
    
    #Función para obtener la instancia del formulario
    def get_instance(self, form_name):
        instance_method = 'get_%s_instance' % form_name
        if hasattr(self, instance_method):
            return getattr(self, instance_method)()
        else:
            return None

    def forms_valid(self, forms, form_name):
        form_valid_method = '%s_form_valid' % form_name
        if hasattr(self, form_valid_method):
            return getattr(self, form_valid_method)(forms[form_name])
        else:
            return HttpResponseRedirect(self.get_success_url(form_name))
    
    def forms_invalid(self, forms):
        return self.render_to_response(self.get_context_data(forms=forms))
    
    def get_initial(self, form_name):
        initial_method = 'get_%s_initial' % form_name
        if hasattr(self, initial_method):
            attrs = getattr(self, initial_method)()
            attrs['action'] = form_name
            return attrs
        else:
            return {'action': form_name}
    
    #Función para obtener el prefix de cada formulario
    def get_prefix(self, form_name):
        return self.prefixes.get(form_name, self.prefix)
    
    #Función para recoger la url de cada formulario(Se usa cuando cada formulario redirecciona a una url diferente)
    def get_success_url(self, form_name=None):
        return self.success_urls.get(form_name, self.success_url)
    
    #Función para crear los formularios 
    def _create_form(self, form_name, form_class):
        form_kwargs = self.get_form_kwargs(form_name)

        #Se pide la variable de sesión que contiene el ID del perfil del usuario
        idUsuario = self.request.session.get('idUserP')
        #Se pide la variable de sesión que contiene el ID del perfil del usuario
        idUser = self.request.session.get('idUser')


        if form_name == 'datospersona':
            datos = get_object_or_404(DatosUsua,pk=idUsuario)
            form = form_class(**form_kwargs,instance=datos)
            return form
        elif form_name == 'experienciasForm':
            formset = form_class(**form_kwargs,queryset = Experiencia.objects.filter(IdUsuarios=idUsuario))
            return formset
        elif form_name == 'habilidadesForm': 
            formset = form_class(**form_kwargs,queryset = Habilidad.objects.filter(IdUsuarios=idUsuario))
            return formset
        elif form_name == 'logrosForm':
            formset =  form_class(**form_kwargs, queryset = Logro.objects.filter(IdUsuarios=idUsuario))
            return formset
        elif form_name == 'educacionesForm':
            formset = form_class(**form_kwargs, queryset = Educacion.objects.filter(IdUsuarios=idUsuario))
            return formset
        elif form_name == 'usuarioForm':
            datos = get_object_or_404(User,id=idUser)
            form = form_class(**form_kwargs,instance=datos)
            return form
        elif form_name == 'perfilForm':
            datos = get_object_or_404(Perfil,pk=idUsuario)
            form = form_class(**form_kwargs,instance=datos)
            return form                             
        else:
            form = form_class(**form_kwargs)
            return form

    

class ProcessMultipleFormsView(ProcessFormView):
    
    #Función para recoger los datos GET 
    def get(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        return self.render_to_response(self.get_context_data(forms=forms))

    #Función para recoger los datos POST que se mandaron y el ID del usuario
    def post(self, request, *args, **kwargs):

        #Se pide el nombre del formulario
        form_name = self.request.POST.get('formName')

        #Se pide la variable de sesión que contiene el ID del perfil del usuario
        form_IdUser = self.request.session.get('idUserP')

        #Se pide la variable de sesión que contiene el ID del usuario
        user = self.request.session.get('idUser')
        
        #En caso de que se vayan a guardar los formularios de la hoja de vida
        if form_name == 'multiForm':
            return self._redirect_multiple_forms(request,form_IdUser)
        #En caso de que se vayan a guardar los formularios de usuario y perfil
        elif form_name == 'userForm':
            return self._redirect_user_forms(request,user,form_IdUser)
        else:
        #Si el formulario no existe
            return HttpResponseForbidden()
    
    #Función para redireccionar a la función para validar y procesar varios formularios
    def _redirect_multiple_forms(self,request,form_IdUser):
        form_valid_method = 'multipleForm_form_valid'
        if hasattr(self, form_valid_method):
            return getattr(self, form_valid_method)(self.request,form_IdUser)
        else:
            return HttpResponseRedirect('update?Id=1')
    
    #Función para redireccionar a la función para validar y procesar los formularios de usuario
    def _redirect_user_forms(self,request,user,id_perfil):
        form_valid_method = 'user_form_valid'
        if hasattr(self, form_valid_method):
            return getattr(self, form_valid_method)(self.request,user,id_perfil)
        else:
            return HttpResponseRedirect('update?Id=1')
       
    #Función para procesar un sólo formulario
    def _process_individual_form(self, form_name, form_classes):
        forms = self.get_forms(form_classes)
        form = forms.get(form_name)
        if not form:
            return HttpResponseForbidden()
        if form.is_valid():
            return self.forms_valid(forms, form_name)
        else:
            return self.forms_invalid(forms)
 
 
class BaseMultipleFormsView(MultiFormMixin, ProcessMultipleFormsView):
    """
    A base view for displaying several forms.
    """
 
class MultiFormsView(TemplateResponseMixin, BaseMultipleFormsView):
    """
    A view for displaying several forms, and rendering a template response.
    """