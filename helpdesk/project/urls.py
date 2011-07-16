from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    # Example:
    # (r'^helpdesk/', include('helpdesk.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Admin tools
    url(r'^admin_tools/', include('admin_tools.urls')),

    # Auth
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}, 'login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'auth/logout.html'}, 'logout'),

    # Soporte
    (r'', include('soporte.urls')),

)

if settings.DEBUG:
    from django.views.static import serve

    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$',
            serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        url(r'^media/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

