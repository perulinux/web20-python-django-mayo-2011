#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^latest/$', views.latest_books),
)

