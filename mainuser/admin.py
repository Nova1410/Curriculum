from django.contrib import admin

from .models import DatosUsua
from .models import Logro
from .models import Educacion
from .models import Habilidad
from .models import Experiencia
from .models import Cargo

# Register your models here.
class DatosUsuaModelAdmin(admin.ModelAdmin):
    list_display = ('IdUsuarios','IdEtnias','Genero',)
    list_display_links = ('IdUsuarios',)
    list_filter = ('IdUsuarios',)
    search_fields = ('IdUsuarios',)
    class Meta:
        model = DatosUsua

admin.site.register(DatosUsua,DatosUsuaModelAdmin)

class EducModelAdmin(admin.ModelAdmin):
    list_display = ('Instituto','Titulo','FechGrado',)
    list_display_links = ('Instituto',)
    list_filter = ('Titulo',)
    search_fields = ('FechGrado',)
    class Meta:
        model = Educacion

admin.site.register(Educacion,EducModelAdmin)

class HabilidadModelAdmin(admin.ModelAdmin):
    list_display = ('NombHabil', 'NiveHabil',)
    list_filter = ('NiveHabil',)
    search_fields = ('NombHabil',)
    class Meta:
        model = Habilidad

admin.site.register(Habilidad, HabilidadModelAdmin)

class ExperienciaModelAdmin(admin.ModelAdmin):
    list_display = ('Empresa', 'Funciones', 'Logros',)
    list_display_links = ('Empresa', 'Funciones',)
    search_fields = ('Empresa',)
    list_fields = ('idExperiencia',)
    class Meta:
        model = Experiencia

admin.site.register(Experiencia,ExperienciaModelAdmin)

class LogrosModelAdmin(admin.ModelAdmin):
    list_display = ('NombrLogr', 'DescLogr',)
    list_display_links = ('NombrLogr',)
    search_fields = ('NombrLogr',)
    list_filter = ('NombrLogr',)
admin.site.register(Logro, LogrosModelAdmin)

