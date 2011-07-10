from django.contrib import admin
from software.models import FamiliaSoftware
from software.models import Software

class FamiliaSoftwareAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado_en', )
    search_fields = ('nombre', )
    ordering = ('id', )

admin.site.register(FamiliaSoftware, FamiliaSoftwareAdmin)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'familia', 'fabricante', 'sistema_operativo','creado_en', )
    search_fields = ('nombre', 'fabricante', )
    ordering = ('id', )
    list_filter = ('familia', 'fabricante', )

admin.site.register(Software, SoftwareAdmin)

