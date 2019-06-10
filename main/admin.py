from django.contrib import admin
from .models import Experiencia

# Register your models here.
class ExperienciaModelAdmin(admin.ModelAdmin):
    list_display = ('Empresas', 'Funciones', 'Logros' )
    list_display_links = ('Empresa', 'Funciones')
    search_fields = ('Empresa')
    list_fields = ('idExperiencia')

admin.site.register(Experiencia)
