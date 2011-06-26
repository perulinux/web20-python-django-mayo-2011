#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext as _

class Author(models.Model):

    firstname = models.CharField(
        verbose_name=_(u'Nombres'),
        max_length=60
    )

    lastname = models.CharField(
        verbose_name=_(u'Apellidos'),
        max_length=60
    )

    website = models.URLField(
        verbose_name=_(u'Sitio web'),
        verify_exists=False,
        null=True,
        blank=True
    )

    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)

    class Meta:
        verbose_name = _(u'Autor')
        verbose_name_plural = _(u'Autores')
        ordering = ('lastname', 'firstname', )

class Book(models.Model):

    title = models.CharField(
        verbose_name=_(u'Título'),
        max_length=50
    )

    author = models.ForeignKey(Author,
        verbose_name=_(u'Autor')
    )

    pub_date = models.DateField(
        verbose_name=_(u'Fecha de publicación')
    )

    stock = models.PositiveIntegerField(
        verbose_name=_(u'Stock'),
        help_text=_(u'Cantidad de items en stock')
    )

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = _(u'Libro')
        verbose_name_plural = _(u'Libros')
        ordering = ('title', 'pub_date', )

class Order(models.Model):

    firstname = models.CharField(
        verbose_name=_(u'Nombres'),
        max_length=60
    )

    lastname = models.CharField(
        verbose_name=_(u'Apellidos'),
        max_length=60
    )
 
    email = models.EmailField(
        verbose_name=_(u'Correo electrónico')
    )
     
    book = models.ForeignKey(Book,
        verbose_name=_(u'Libro solicitado')
    )

    copies = models.PositiveIntegerField(
        verbose_name=_(u'Número de copias')
    )

    order_date = models.DateTimeField(
        verbose_name=_(u'Fecha y hora del pedido'),
        auto_now_add=True,
        editable=False
    )

    def __unicode__(self):
        return u'Pedido Nro. %d' % self.id

    class Meta:
        verbose_name = _(u'Pedido')
        verbose_name_plural = _(u'Pedidos')
        ordering = ('order_date', )
