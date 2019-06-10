from django.contrib import admin

from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import TipoEstu
from .models import TipoLogr
from .models import Cargos
from .models import Logros

# Register your models here.
admin.site.register(Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(TipoEstu)
admin.site.register(TipoLogr)
class CargoModelAdmin(admin.ModelAdmin):
    list_display = ('NOMBRE', 'ES CARGO')
    list_display_links = ('NOMBRE')
    search_fields = ('NOMBRE')
    list_filter = ('ES CARGO')
admin.site.register(Cargos)

class LogrosModelAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Descripcion')
    list_display_links = ('Nombre')
    search_fields = ('Nombre')
    list_filter = ('Nombre')
admin.site.register(Logros)