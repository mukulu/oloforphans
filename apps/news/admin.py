from django.contrib import admin
from apps.news.models import *

class NewsAdmin(admin.ModelAdmin):
	list_display = ("title","heading","author","date_posted","expiry_date")

admin.site.register(News,NewsAdmin)
