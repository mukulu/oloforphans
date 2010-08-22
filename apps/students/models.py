from django.db import models
from django.conf import settings

from apps.school_classes.models import SchoolClass

class Person(models.Model):
	"""
		Holds information about people in the system
		and collection methods to process those informations
	"""
	first_name = models.CharField(max_length=128)
	middle_name = models.CharField(null=True,blank=True,max_length=128)
	last_name = models.CharField(max_length=128)
	e_mail = models.EmailField(null=True,blank=True,max_length=128)
	photo = models.ImageField(null=True,blank=True,upload_to=settings.PHOTO_DIR, help_text="Recent Photo")
	birthdate = models.DateField(null=True,blank=True,help_text="Your date of birth")
	birthplace = models.CharField(null=True,blank=True,max_length=128, help_text="Place you were born")	
	
	class Meta:
		ordering = ['first_name','last_name',]
	
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

class Student(models.Model):
	"""
		@Should we put form for stream, or just an entrance year?
		if we put entrance year, we might need to know if he/she's o-level
		or a-level to know which form he is.
	"""
	form = models.ForeignKey(SchoolClass,help_text="Form/Stream you are in.")
	favorite_subject = models.CharField(null=True,blank=True,max_length=128,help_text="Favorite subject")
	future_dream = models.TextField(null=True,blank=True,help_text="Dreams of your future")
	parents = models.CharField(max_length=128,null=True,blank=True)
	guardians = models.CharField(max_length=128,null=True,blank=True,help_text="Names of your guardians")
	about_her = models.TextField(null=True,blank=True,help_text="About her")
	hobbies = models.TextField(null=True, blank=True,help_text="Activity or interests you do for pleasure")
