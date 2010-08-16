from django.contrib import admin

from apps.pages.models import Page, Category

class PageAdmin(admin.ModelAdmin):
	list_display=("heading","name","category","author","date_posted")
	
	class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/tiny_mce/textareas.js',)


class CategoryAdmin(admin.ModelAdmin):
	list_display=("name","description")

admin.site.register(Page,PageAdmin)
admin.site.register(Category,CategoryAdmin)
