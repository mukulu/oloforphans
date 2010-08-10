from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128,help_text="Category of the page")
	parent = models.ForeignKey('Category')
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = "categories"

class Content(models.Model):
	title = models.CharField(null=False, blank=False,max_length=128,help_text="title of the contents")
	heading = models.CharField(max_length=128,help_text="heading of the contents")
	mainbody = models.TextField(max_length=128,help_text="text field of the contents")
	date_posted = models.DateTimeField()
	def __unicode__(self):
		return self.title
	
class Page(Content):
	category = models.ForeignKey('Category')
	author = models.CharField(max_length=128,help_text="Author of the page")
	def __unicode__(self):
		return self.title
