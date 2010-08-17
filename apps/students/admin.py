from django.contrib import admin
from apps.students.models import Person, Student

class PersonAdmin(admin.ModelAdmin):
	list_display=("photo","user","birthdate","birthplace")

class StudentAdmin(admin.ModelAdmin):
	list_display=("photo","user","birthdate","birthplace","form")
	fieldsets = (
		('Basic User Information', {
			'fields': ('user','birthdate','birthplace','form','photo')
			}),
		('Relationships', {
			'classes': ('collapse',),
			'fields': ('parents','siblings','guardians',)
		}),
		('Hobbies and Favorites', {
			'classes': ('collapse',),
			'fields':('hobbies','favorite_subject','future_dream')
		}),
		('Detailed informations', {
			'classes': ('collapse',),
			'fields':('about_her','explanation','quotes')
		}),
	)

admin.site.register(Person,PersonAdmin)
admin.site.register(Student,StudentAdmin)
