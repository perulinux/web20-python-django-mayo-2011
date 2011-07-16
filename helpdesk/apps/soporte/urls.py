# -*- encoding: utf8 -*-

from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^dashboard/$', views.dashboard, {}, 'dashboard'),
    (r'^mis_incidencias/$', views.mis_incidencias, {}, 'mis_incidencias'),
    (r'^incidencias/$', views.incidencias, {}, 'incidencias'),
)
