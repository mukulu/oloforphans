from datetime import datetime

from django.db import models

class News(models.Model):
    heading = models.CharField(max_length=256, help_text="Write the title of the news")
    Content = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(default = datetime.now)
    
    def __init__(self):
        return '%s (%s)' % (self.heading, self.created_date)    