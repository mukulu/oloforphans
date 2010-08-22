from datetime import datetime

from django.db import models
from django.conf import settings
from apps.news.utils import endtime

class News(models.Model):
	"""
		News, shows news to be viewed. 
	"""
	heading = models.CharField(max_length=128, unique=True)
	# TODO put a default image.
	photo = models.ImageField(upload_to=settings.PHOTO_DIR,null=True, blank=True)
	content = models.TextField(help_text="The news contents goes here")
	author = models.CharField(max_length=128)
	date_posted = models.DateTimeField(default = datetime.now,auto_now=True)
	expiry_date = models.DateTimeField(default = endtime, help_text="The date news should be considered expired")
	
	class Meta:
			ordering = ['-date_posted','heading']
			verbose_name_plural = 'News'
	
	def __unicode__(self):
		return self.heading
