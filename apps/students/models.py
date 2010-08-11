from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Person(models.Model):
	"""
		Holds information about people in the system
		and collection methods to process those informations
		
		@I have used PHOTO_DIR declared in settings.py, not sure if it
		 needs any imports to use settings from settings.py
	"""
	user = models.ForeignKey(User, unique=True)
	photo = models.ImageField(null=True,upload_to=settings.PHOTO_DIR, help_text="Recent Photo")
	birthdate = models.DateField(help_text="Your date of birth")
	birthplace = models.CharField(max_length=128, help_text="Place you were born")
	hobbies = models.TextField(null=True, blank=True,help_text="Activity or interesest you do for pleasure")
	sibblings = models.TextField(null=True,blank=True,help_text="Your kinsman, next of kin, persons of near relationship")
	
	def __unicode__(self):
		return self.user.username

class Student(Person):
	"""
		@Should we put form for stream, or just an entrance year?
		if we put entrance year, we might need to know if he/she's o-level
		or a-level to know which form he is.
	"""
	form = models.CharField(max_length=128,help_text="Form/Stream you are in.")
	favorite_subject = models.CharField(max_length=128,help_text="Favorite subject")
	future_dream = models.TextField(null=True,blank=True,help_text="Dreams of your future")
	parents = models.TextField(null=True,blank=True,help_text="Names of your parents")
	guardians = models.TextField(null=True,blank=True,help_text="Names of your guardians")
	explanation = models.TextField(null=True,blank=True,help_text="How she came to bethsaida")
	about_her = models.TextField(null=True,blank=True,help_text="About her")
	quotes = models.TextField(null=True,blank=True,help_text="Quotes from student")
