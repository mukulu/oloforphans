from django.contrib import admin
from apps.news.models import News

class NewsAdmin(admin.ModelAdmin):
	date_hierarchy = 'date_posted'
	list_display = ("heading","author","date_posted","expiry_date")
	list_filter = ('author',)
	
	fieldsets = (
        ('Heading', {
            'fields': ('heading',)
        }),
        ('Contents', {
			'fields':('photo', 'content','author')
		}),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('date_posted','expiry_date')
        }),
    )



admin.site.register(News,NewsAdmin)
