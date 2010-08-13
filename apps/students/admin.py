from django.contrib import admin
from apps.students.models import Person, Student
from django.contrib.auth.models import User

class PersonAdmin(admin.ModelAdmin):
	list_display=("username","firstname","lastname")

class UserInline(admin.TabularInline):
	model = Student
	extra = 1

class StudentAdmin(admin.ModelAdmin):
	pass
#	list_display=("photo","user","birthdate","birthplace","form")
#	inlines = [UserInline,]
#	fieldsets = (
#        ('Basic User Information', {
#            'fields': ('birthdate','birthplace','form','photo')
#        }),
#        ('Hobbies and Favorites', {
#			'classes': ('collapse',),
#			'fields':('hobbies','favorite_subject','future_dream')
#		}),
#		('Detailed informations', {
#			'classes': ('collapse',),
#			'fields':('about_her','explanation','quotes')
#		}),
#        ('Relationships', {
#            'classes': ('collapse',),
#            'fields': ('parents','siblings','guardians',)
#        }),
#    )

admin.site.register(Student,StudentAdmin)
