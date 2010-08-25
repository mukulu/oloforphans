from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from cms.sitemaps import CMSSitemap
from apps.news import urls as news_urls
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^oloforphans/', include('oloforphans.foo.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/javascripts'}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('cms.urls')),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    (r'', include(news_urls)),
)
