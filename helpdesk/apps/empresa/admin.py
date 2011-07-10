# -*- encoding: utf8 -*-

from django.contrib import admin
from empresa.models import Proveedor
from empresa.models import Empleado
from empresa.models import Area

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'website', )
    search_fields = ('nombre', 'direccion', 'telefonos', )
    ordering = ('nombre', )

admin.site.register(Proveedor, ProveedorAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'apepat', 'apemat','nombres','area' )
    search_fields = ('apepat','apemat','nombres', 'direccion', 'telefonos', )
    list_filter = ('area', )
    ordering = ('apepat','apemat','nombres', )

admin.site.register(Empleado, EmpleadoAdmin)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'responsable', 'anexo', )
    search_fields = ('nombre', 'responsable', 'anexo', )
    ordering = ('nombre', )

admin.site.register(Area, AreaAdmin)
