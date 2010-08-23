from django.contrib import admin
from apps.students.models import Person, Student

class PersonAdmin(admin.ModelAdmin):
	list_display=("photo","birthdate","birthplace")

class StudentAdmin(admin.ModelAdmin):
	list_display=("first_name","middle_name","last_name","birthdate","birthplace","form")
	search_fields=['first_name','middle_name','last_name','birthplace',"e_mail"]
	fieldsets = (
		('Basic User Information', {
			'classes': ['extrapretty'],
			'fields': ('first_name','middle_name','last_name','birthdate','birthplace','form','photo')
			}),
		('Guardianship', {
			'classes': ('collapse',),
			'fields': ('parents','guardians',)
		}),
		('Hobbies and Favorites', {
			'classes': ('collapse',),
			'fields':('future_dream','hobbies','favorite_subject',)
		}),
		('Detailed informations', {
			'classes': ('collapse',),
			'fields':('about_her',)
		}),
	)

#admin.site.register(Person,PersonAdmin)
admin.site.register(Student,StudentAdmin)
