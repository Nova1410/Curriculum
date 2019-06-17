from django.contrib import admin

from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import TipoEstu
from .models import TipoLogr
from .models import Cargo

# Register your models here.
class EtniaModelAdmin(admin.ModelAdmin):
    list_display = ('NombEtni',)
    list_display_links = ('NombEtni',)
    list_filter = ('NombEtni',)
    search_fields = ('NombEtni',)
    class Meta:
        model = Etnia
admin.site.register(Etnia,EtniaModelAdmin)

class TipoDocuModelAdmin(admin.ModelAdmin):
    list_display = ('NombTiDo',)
    list_display_links = ('NombTiDo',)
    list_filter = ('NombTiDo',)
    search_fields = ('NombTiDo',)
    class Meta:
        model = TipoDocu
admin.site.register(TipoDocu,TipoDocuModelAdmin)

class EstaCivilModelAdmin(admin.ModelAdmin):
    list_display = ('NombEsCi',)
    list_display_links = ('NombEsCi',)
    list_filter = ('NombEsCi',)
    search_fields = ('NombEsCi',)
    class Meta:
        model = EstaCivil
admin.site.register(EstaCivil,EstaCivilModelAdmin)

class TipoEstuModelAdmin(admin.ModelAdmin):
    list_display = ('NombTiEs',)
    list_display_links = ('NombTiEs',)
    list_filter = ('NombTiEs',)
    search_fields = ('NombTiEs',)
    class Meta:
        model = TipoEstu
admin.site.register(TipoEstu,TipoEstuModelAdmin)

class TipoLogrModelAdmin(admin.ModelAdmin):
    list_display = ('NombTiLo',)
    list_display_links = ('NombTiLo',)
    list_filter = ('NombTiLo',)
    search_fields = ('NombTiLo',)
    class Meta:
        model = TipoLogr
admin.site.register(TipoLogr,TipoLogrModelAdmin)

class CargoModelAdmin(admin.ModelAdmin):
    list_display = ('NombCarg','EsCargo',)
    list_display_links = ('NombCarg',)
    list_filter = ('EsCargo',)
    search_fields = ('NombCarg',)
    class Meta:
        model = Cargo

admin.site.register(Cargo,CargoModelAdmin)


