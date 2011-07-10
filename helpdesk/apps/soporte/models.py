#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.fields import CreationDateTimeField
from empresa.models import Proveedor
from empresa.models import Empleado
from hardware.models import Equipo
from software.models import Software

class Incidencia(models.Model):

    GRAVEDAD_BAJA = 0
    GRAVEDAD_MEDIA = 1
    GRAVEDAD_ALTA = 2
    GRAVEDAD_MUY_ALTA = 3

    GRAVEDAD_CHOICES = (
        (GRAVEDAD_BAJA, _(u'Baja')),
        (GRAVEDAD_MEDIA, _(u'Media')),
        (GRAVEDAD_ALTA, _(u'Alta')),
        (GRAVEDAD_MUY_ALTA, _(u'Muy alta')),
    )

    ESTADO_REPORTADA = 0
    ESTADO_CONFIRMADA = 1
    ESTADO_CANCELADA = 2
    ESTADO_RECHAZADA = 3
    ESTADO_POR_ATENDER = 4 
    ESTADO_EN_CURSO = 5
    ESTADO_EN_PAUSA = 6
    ESTADO_SOLUCIONADA = 7
    ESTADO_ACEPTADA = 8

    ESTADO_CHOICES = (
        (ESTADO_REPORTADA, _(u'Reportada')),
        (ESTADO_CONFIRMADA, _(u'Confirmada')),
        (ESTADO_CANCELADA, _(u'Cancelada')),
        (ESTADO_RECHAZADA, _(u'Rechazada')),
        (ESTADO_POR_ATENDER, _(u'Por atender')),
        (ESTADO_EN_CURSO, _(u'En curso')),
        (ESTADO_EN_PAUSA, _(u'En pausa')),
        (ESTADO_SOLUCIONADA, _(u'Solucionada')),
        (ESTADO_ACEPTADA, _(u'Aceptada')),
    )

    AVANCE_CHOICES = (
        (0.00, _(u'0%')),
        (0.10, _(u'10%')),
        (0.20, _(u'20%')),
        (0.30, _(u'30%')),
        (0.40, _(u'40%')),
        (0.50, _(u'50%')),
        (0.60, _(u'60%')),
        (0.70, _(u'70%')),
        (0.80, _(u'80%')),
        (0.90, _(u'90%')),
        (1.00, _(u'100%')),
    )

    titulo = models.CharField(
        verbose_name=_(u'Título'),
        max_length=255,
    )

    gravedad = models.PositiveIntegerField(
        verbose_name=_(u'Gravedad'),
        choices=GRAVEDAD_CHOICES
    )

    estado = models.PositiveIntegerField(
        verbose_name=_(u'Estado'),
        choices=ESTADO_CHOICES
    )

    descripcion = models.TextField(
        verbose_name=_(u'Descripción'),
    )

    reportada_por = models.ForeignKey(Empleado,
        verbose_name=_(u'Reportada por'),
        related_name='incidencias_reportadas'
    )

    asignada_a = models.ForeignKey(Empleado,
        verbose_name=_(u'Asignada a'),
        related_name='incidencias_asignadas',
        null=True,
        blank=True
    )

    avance = models.FloatField(
        verbose_name=_(u'Porcentaje de avance'),
        choices=AVANCE_CHOICES,
        default=0.00
    )

    equipo = models.ForeignKey(Equipo,
        verbose_name=_(u'Equipo'),
        null=True,
        blank=True
    )

    software = models.ManyToManyField(Software,
        verbose_name=_(u'Software'),
        null=True,
        blank=True
    )

    creado_en = CreationDateTimeField(
        verbose_name=_(u'Creado en')
    )
       
    def __unicode__(self):
        return u'Incidencia #%d: %s' % (
            self.id, 
            self.titulo
        )
    
    class Meta:
        verbose_name = _(u'Incidencia')
        verbose_name_plural = _(u'Incidencias')
        ordering = ('creado_en', )

class Evento(models.Model):

    incidencia = models.ForeignKey(Incidencia,
        verbose_name=_(u'Incidencia')
    )

    mensaje = models.TextField(
        verbose_name=_(u'Mensaje'),
    )

    metadatos = models.TextField(
        verbose_name=_(u'Metadatos'),
        help_text=_(u'Datos no estructurados en formato JSON'),
        blank=True, 
        null=True
    )

    creado_en = CreationDateTimeField()

    def __unicode__(self):
        return u'Evento #%d: %s' % (
            self.id, 
            self.mensaje
        )

    class Meta:
        verbose_name = _(u'Evento')
        verbose_name_plural = _(u'Eventos')
        ordering = ('creado_en', )


class Adjunto(models.Model):

    incidencia = models.ForeignKey(Incidencia,
        verbose_name=_(u'Incidencia')
    )

    archivo = models.FileField(
        verbose_name=_(u'Nombre de archivo'),
        upload_to='archivos/'
    )

    creado_en = CreationDateTimeField(
        verbose_name=_(u'Creado en')
    )

    def __unicode__(self):
        return u'Archivo %d (Incidencia %d)' % (
            self.id,
            self.incidencia.id
        )
    
    class Meta:
        verbose_name = _('Adjunto')
        verbose_name_plural = _('Adjuntos')
