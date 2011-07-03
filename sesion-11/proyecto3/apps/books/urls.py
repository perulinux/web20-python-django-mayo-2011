#!/usr/bin/env python
# -*- encoding: utf8 -*-

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^/?$', views.create_order, {}, 'create_order'),
    (r'^latest/$', views.latest_books, {}, 'latest_books'),
)
