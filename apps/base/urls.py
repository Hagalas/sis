"""urlconf for the base application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('apps.base.views',
    url(r'^$', 'home', name='home'),
)

from django.conf import settings

# ... your normal urlpatterns here

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))