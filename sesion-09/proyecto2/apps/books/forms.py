#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django import forms
from django.utils.translation import ugettext as _
from models import Order

class OrderForm(forms.ModelForm):

    def clean(self):
        data = self.cleaned_data
        if 'copies' in data and 'book' in data:
            copies = data['copies']
            book = data['book']
            if book.stock < copies:
                msg = _(u'No existen suficientes copias en stock')
                raise forms.ValidationError(msg)
        return data

    def save(self, *args, **kwargs):
        # We decrement the number of items in stock
        # for the requested book
        book = self.cleaned_data['book']
        copies = self.cleaned_data['copies']
        book.stock -= copies
        book.save()
        return super(OrderForm, self).save(*args, **kwargs)

    class Meta:
        model = Order

