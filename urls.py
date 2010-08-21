from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from apps.news import urls as news_urls
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^oloforphans/', include('oloforphans.foo.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/javascripts'}),
    (r'^statics/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
    (r'', include(news_urls)),
)
