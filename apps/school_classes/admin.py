from django.contrib import admin
from apps.school_classes.models import SchoolClass, Subject

class SchoolClassAdmin(admin.ModelAdmin):
    pass

class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)
admin.site.register(SchoolClass,SchoolClassAdmin)
