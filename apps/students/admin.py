from django.contrib import admin
from apps.students.models import *

class PersonAdmin(admin.ModelAdmin):
	list_display=("photo","user","birthdate","birthplace")

class StudentAdmin(admin.ModelAdmin):
	list_display=("photo","user","birthdate","birthplace","form")

admin.site.register(Person,PersonAdmin)
admin.site.register(Student,StudentAdmin)
