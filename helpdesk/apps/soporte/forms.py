# -*- encoding: utf8 -*-

from django import forms
from django.utils.translation import ugettext as _
from soporte.models import Incidencia

class CrearIncidenciaForm(forms.ModelForm):

    def save(self, request, *args, **kwargs):
        incidencia = super(CrearIncidenciaForm, self).save(
            commit=False,*args, **kwargs)
        incidencia.reportada_por=request.user.empleado
        incidencia.estado = Incidencia.ESTADO_REPORTADA
        return super(CrearIncidenciaForm, self).save(*args, **kwargs)

    class Meta:
        model = Incidencia
        exclude = (
            'creado_en',
            'avance',
            'asignada_a',
            'estado',
            'reportada_por'
        )
