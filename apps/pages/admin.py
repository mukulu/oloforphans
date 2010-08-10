from django.contrib import admin
from apps.pages.models import *

class PageAdmin(admin.ModelAdmin):
	pass

class ContentAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Page,PageAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Category,CategoryAdmin)
