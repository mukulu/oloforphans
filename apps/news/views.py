from django.shortcuts import render_to_response
from django.template import RequestContext

#from apps.news.models import News

def home(request):
    #news = News.objects.all()
    return render_to_response(
                                'base.html',
                                {},
                                context_instance = RequestContext(request),
                              )

