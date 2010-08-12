from django.contrib import admin
from apps.pages.models import Page, Content, Category

class PageAdmin(admin.ModelAdmin):
	pass

class ContentAdmin(admin.ModelAdmin):
	pass

class CategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Page,PageAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Category,CategoryAdmin)
