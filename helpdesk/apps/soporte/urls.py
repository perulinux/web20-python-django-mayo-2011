# -*- encoding: utf8 -*-

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^dashboard/$', views.dashboard, {}, 'dashboard'),
)
