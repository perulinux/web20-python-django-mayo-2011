# -*- encoding: utf8 -*-

from django.contrib import admin
from empresa.models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'website', )
    search_fields = ('nombre', 'direccion', 'telefonos', )
    ordering = ('nombre', )

admin.site.register(Proveedor, ProveedorAdmin)
