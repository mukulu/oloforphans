from django.conf.urls.defaults import *
import apps.news.views as views

#from django.conf import settings   
urlpatterns = patterns('',
    # the index view
    url(r'',     views.home, name="home"),
)