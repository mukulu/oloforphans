from django.contrib import admin

from apps.volunteers.models import Volunteer

class VolunteerAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_registered'
    list_display = ('first_name','last_name','sex','nationality','occupation','phone_number','e_mail','date_registered')
    list_filter = ('nationality',)
    fieldsets = (
		("Basic Volunteer's Information", {
			'classes': ['extrapretty'],
			'fields': ('first_name','middle_name','last_name','sex','nationality')
			}),
		('Extra information', {
			'classes': ('collapse',),
			'fields': ('photo','e_mail','phone_number','occupation')
		})
	)
    search_fields=['first_name','middle_name','last_name','nationality']

admin.site.register(Volunteer,VolunteerAdmin)
