#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.db import models
from django.utils.translation import ugettext as _

class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _(u'Book')
        verbose_name_plural = _(u'Books')
        ordering = ('name', 'pub_date', )

