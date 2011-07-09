# -*- encoding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.fields import CreationDateTimeField

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

