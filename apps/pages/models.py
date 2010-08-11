from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
	"""
		We will be using this class to arrange pages into hierarchy
		for displaying on the menubar or sidebar.
		It's recursive, thus menu can have submenus going inward.
	"""
	name = models.CharField(unique=True,max_length=128,help_text="Category of the page")
	parent = models.ForeignKey('Category',null=True)
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = "categories"
		ordering = ['parent']

class Content(models.Model):
	title = models.CharField(null=False, unique=True, blank=False,max_length=128,help_text="title of the contents")
	heading = models.CharField(max_length=128,help_text="heading of the contents")
	mainbody = models.TextField(max_length=128,help_text="text field of the contents")
	date_posted = models.DateTimeField(default=datetime.now)
	author = models.CharField(max_length=128,help_text="Author of the page")
	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['title']
	
class Page(Content):
	category = models.ForeignKey('Category')
	def __unicode__(self):
		return self.title
	class Meta:
			ordering = ['title']
