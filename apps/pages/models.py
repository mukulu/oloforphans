from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128,help_text="Category of the page")
	parent = models.ForeignKey('Category')

class Content(models.Model):
	title = models.CharField(null=False, blank=False,max_length=128,help_text="title of the contents")
	heading = models.CharField(max_length=128,help_text="heading of the contents")
	mainbody = models.TextField(max_length=128,help_text="text field of the contents")
	date_posted = models.DateTimeField()
	
class Page(Content):
	category = models.ForeignKey('Category')
	author = models.CharField(max_length=128,help_text="Author of the page")
	
