from django.conf.urls.defaults import *

from django.contrib import admin
import apps
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^oloforphans/', include('oloforphans.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^apps/news/', include('apps.news.urls')),
    # (r'^apps/pages/', include('apps.pages.urls')),
    # (r'^apps/students/', include('apps.students.urls')),
    # (r'^apps/classes/', include('apps.school_classes.urls')),
    (r'^admin/', include(admin.site.urls)),
)
