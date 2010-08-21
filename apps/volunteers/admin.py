from django.contrib import admin

from apps.volunteers.models import Volunteer

class VolunteerAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_registered'
    list_display = ('first_name','last_name','sex','nationality',)
    list_filter = ('nationality',)

admin.site.register(Volunteer,VolunteerAdmin)