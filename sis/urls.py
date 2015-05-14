""" Default urlconf for sis """

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

