# -*- encoding: utf8 -*-

from django.contrib import admin
from soporte.models import Incidencia
from soporte.models import Evento
from soporte.models import Adjunto

class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'reportada_por', 'estado', 'gravedad', 'creado_en', )
    search_fields = ('titulo', 'reportado_por', )
    ordering = ('id', )

admin.site.register(Incidencia, IncidenciaAdmin)
