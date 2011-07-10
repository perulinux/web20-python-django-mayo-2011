#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.fields import CreationDateTimeField
from empresa.models import Proveedor
from empresa.models import Empleado

class TipoEquipo(models.Model):
    
    nombre = models.CharField(
        verbose_name=_(u'Nombre'),
        max_length=64
    )

    creado_en = CreationDateTimeField(
        verbose_name=_(u'Creado en')
    )
       
    def __unicode__(self):
        return (self.nombre)
    
    class Meta:
        verbose_name = _(u'Tipo de equipo')
        verbose_name_plural = _(u'Tipos de equipo')
        ordering = ('nombre', )

class EquipoManager(models.Manager):

    def activos(self):
        self.filter(estado=Equipo.ESTADO_ACTIVO)

class Equipo(models.Model):
    
    ESTADO_ACTIVO = 1
    ESTADO_INACTIVO = 2

    ESTADO_CHOICES = (
        (ESTADO_ACTIVO, u'Activo'),
        (ESTADO_INACTIVO, u'Inactivo'),
    )

    nombre = models.CharField(
        verbose_name=_(u'Nombre'),
        max_length=64
    )

    tipo = models.ForeignKey(TipoEquipo,
        verbose_name=(u'Tipo de equipo')
    )
    
    descripcion = models.TextField(
        verbose_name=_(u'Descripción'),
        null=True, 
        blank=True
    )
   
    empleado = models.ForeignKey(Empleado,
        verbose_name=_(u'Empleado asignado')
    )
    
    serie = models.CharField(
        verbose_name=_(u'Número de serie'),
        max_length=64,
        blank=True,
        null=True
    )

    fabricante = models.ForeignKey(Proveedor,
        verbose_name=_(u'Fabricante')
    )

    estado = models.PositiveSmallIntegerField(
        verbose_name=_(u'Estado'),
        choices=ESTADO_CHOICES
    )

    creado_en = CreationDateTimeField(
        verbose_name=_(u'Creado en')
    )

    def __unicode__(self):
        return (self.descripcion)
    
    class Meta:
        verbose_name = _(u'Equipo')
        verbose_name_plural = _(u'Equipos')
        ordering = ('nombre', )
        
