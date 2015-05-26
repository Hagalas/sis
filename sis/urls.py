""" Default urlconf for sis """
from django.conf import settings

from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bad/$', bad),
    # url(r'', include('base.urls')),
    url(r'', include('classes.urls')),

)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
