from django.conf.urls import url, patterns
import views

urlpatterns = patterns('classes.views',
    url(r'^schedule/$', 'schedule', name='schedule'),
    url(r'^grades/$', 'grades', name='grades'),
    url(r'^$', 'index', name='index'),
    # url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)