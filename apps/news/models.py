from datetime import datetime

from django.db import models
from apps.pages.models import Content

class News(Content):
	"""
		News share similarity with contents of page app. 
	"""
	expiry_date = models.DateTimeField(help_text="The date news should be considered expired")
	def __unicode__(self):
		return self.title
	class Meta:
			ordering = ['title']
			verbose_name_plural = 'News'

