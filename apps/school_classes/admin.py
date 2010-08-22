from django.contrib import admin

from apps.school_classes.models import SchoolClass, Subject

class SchoolClassAdmin(admin.ModelAdmin):
    list_display=("name",)
    filter_horizontal=("subjects",)

class SubjectAdmin(admin.ModelAdmin):
    list_display=("name","description")

admin.site.register(Subject, SubjectAdmin)
admin.site.register(SchoolClass,SchoolClassAdmin)
