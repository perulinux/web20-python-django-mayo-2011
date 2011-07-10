#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.fields import CreationDateTimeField
from empresa.models import Proveedor

class FamiliaSoftware(models.Model):
    
    nombre = models.CharField(
        verbose_name=_(u'Nombre'),
        max_length=64,
        unique=True
    )

    creado_en = CreationDateTimeField(
        verbose_name=_(u'Creado en')
    )
       
    def __unicode__(self):
        return (self.nombre)
    
    class Meta:
        verbose_name = _(u'Familia de software')
        verbose_name_plural = _(u'Familias de software')
        ordering = ('nombre', )

class Software(models.Model):
    
    nombre = models.CharField(
        verbose_name=_(u'Nombre'),
        max_length=64,
        unique=True
    )

    familia = models.ForeignKey(FamiliaSoftware,
        verbose_name=_(u'Familia')
    )

    fabricante = models.ForeignKey(Proveedor,
        verbose_name=_(u'Fabricante')
    )

    descripcion = models.TextField(
        verbose_name=_(u'Descripción'),
        null=True, 
        blank=True
    )

    sistema_operativo = models.BooleanField(
        verbose_name=_(u'¿Es sistema operativo?'),
        default=True
    )

    creado_en = CreationDateTimeField(
        verbose_name=_(u'Creado en')
    )
       
    def __unicode__(self):
        return (self.nombre)
    
    class Meta:
        verbose_name = _(u'Software')
        verbose_name_plural = _(u'Software')
        ordering = ('nombre', )
