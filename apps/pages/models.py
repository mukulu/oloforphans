from django.db import models
from datetime import datetime

class Category(models.Model):
	"""
		We will be using this class to arrange pages into menus or tabs
		which will be holding links to pages.
		For now it's not going to be recursive
	"""
	name = models.CharField(unique=True,max_length=128,help_text="Category of the page")
	description = models.TextField(null=True,blank=True,help_text="A little explanation on\
					what kind of pages fall under this category")
	#parent = models.ForeignKey('Category',related_name="children", null=True, blank=True)

	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name = "Page tab"
		verbose_name_plural = "Page tabs"
		ordering = ['name']

class Content(models.Model):
	heading = models.CharField(max_length=128,help_text="heading of the contents")
	content = models.TextField(null=True,blank=True,help_text="text field of the contents")
	date_posted = models.DateTimeField(default=datetime.now,auto_now=True)
	author = models.CharField(max_length=128,help_text="Author of the page")
	
	def __unicode__(self):
		return self.heading
	
	class Meta:
		ordering = ['heading']
	
class Page(Content):
	name = models.CharField(null=False, unique=True, blank=False,max_length=128,help_text="The name/nickname for url that leads to the page.(appears on menu)")
	url = models.URLField(null=True,blank=True, verify_exists=False,max_length=256,help_text="The URL for page request")
	category = models.ForeignKey(Category)
	
	def __unicode__(self):
		return self.heading
	
	class Meta:
			ordering = ['heading']
