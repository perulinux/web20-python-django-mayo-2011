# -*- encoding: utf8 -*-

from django.contrib import admin
from hardware.models import TipoEquipo
from hardware.models import Equipo

class TipoEquipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado_en', )
    search_fields = ('nombre', )
    ordering = ('id', )

admin.site.register(TipoEquipo, TipoEquipoAdmin)

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'fabricante', 'serie', 'estado', 'creado_en', )
    search_fields = ('nombre', 'fabricante', 'serie', )
    ordering = ('id', )
    list_filter = ('tipo', 'fabricante', )

admin.site.register(Equipo, EquipoAdmin)
