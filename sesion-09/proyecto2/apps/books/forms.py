#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.forms import ModelForm
from models import Order

class OrderForm(ModelForm):

    class Meta:
        model = Order

