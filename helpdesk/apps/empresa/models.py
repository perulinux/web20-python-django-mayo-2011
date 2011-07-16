# -*- encoding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.fields import CreationDateTimeField
from django.contrib.auth.models import User

class Proveedor(models.Model):
    nombre = models.CharField(max_length=64)
    website = models.URLField(verify_exists=False)
    direccion = models.TextField(blank=True, null=True)
    telefonos = models.TextField(blank=True, null=True)
    creado_en = CreationDateTimeField()

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        verbose_name = _(u'Proveedor')
        verbose_name_plural = _(u'Proveedores')
        ordering = ('nombre', )

class Area(models.Model):

    nombre = models.CharField(
        verbose_name = _(u'Nombre'),
        max_length=64,
        unique=True
    )

    anexo = models.CharField(
        verbose_name = _(u'Anexo'),
        max_length=24,
        null=True,
        blank=True
    )

    responsable = models.ForeignKey('Empleado',
        verbose_name = _(u'Responsable'),
        related_name = 'responsables',
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = _(u'Area')
        verbose_name_plural = _(u'Areas')

class Empleado(models.Model):

    TIPO_DNI = 0
    TIPO_CE = 1
    TIPO_PASAPORTE = 2

    TIPO_DOCUMENTO_CHOICES = (
        (TIPO_DNI, _(u'DNI')),
        (TIPO_CE, _(u'Carnet de extranjería')),
        (TIPO_PASAPORTE, _(u'Pasaporte')),
    )

    GENERO_MASCULINO = 0
    GENERO_FEMENINO = 1

    GENERO_CHOICES = (
        (GENERO_MASCULINO, _(u'Masculino')),
        (GENERO_FEMENINO, _(u'Femenino'))
    )

    doc = models.CharField(
        verbose_name=_(u'Número de documento'),
        max_length=8
    )

    tipo_doc = models.PositiveIntegerField(
        choices=TIPO_DOCUMENTO_CHOICES
    )

    nombres = models.CharField(
        verbose_name=_(u'Nombres'),
        max_length=64
    )

    apepat = models.CharField(
        verbose_name=_(u'Apellido paterno'),
        max_length=64
    )

    apemat = models.CharField(
        verbose_name=_(u'Apellido materno'),
        max_length=64
    )
    
    genero = models.PositiveIntegerField(
        verbose_name=_(u'Género'),
        choices=GENERO_CHOICES
    )

    telefonos = models.TextField(
        verbose_name=_(u'Teléfonos'),
        null=True,
        blank=True
    )

    fecha_nac = models.DateField(
        verbose_name=_(u'Fecha de nacimiento'),
        null=True,
        blank=True
    )

    area = models.ForeignKey(Area,
        verbose_name=_(u'Area donde labora')
    )

    superior = models.ForeignKey('Empleado',
        verbose_name=_(u'Superior inmediato'),
        blank=True,
        null=True
    )

    soporte = models.BooleanField(
        verbose_name=_(u'¿Personal de soporte?'),
        default=False,
    )

    usuario = models.OneToOneField(User,
        verbose_name=_(u'Usuario'),
        null=True,
        blank=True
    )

    def __unicode__(self):
        return u'%s (%s)' % (
            self.nombre_completo(),
            self.doc
        )

    class Meta:
        verbose_name = _(u'Empleado')
        verbose_name_plural = _(u'Empleados')
        ordering = ('apepat','apemat', 'nombres', )
        unique_together = (('doc', 'tipo_doc'), )

    def nombre_completo(self):
        return '%s %s, %s' % (
            self.apepat,
            self.apemat,
            self.nombres
        )
