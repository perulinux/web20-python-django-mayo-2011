#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.contrib import admin
from models import *
from django.contrib.auth.models import Permission

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Permission)
