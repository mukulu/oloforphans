from datetime import datetime

from django.db import models

class Volunteer(models.Model):
    """
        A volunteer is any person willing to offer his/her service to the 
        center, and spend some time at the center.
    """
    SEX_CHOICES = (
                    ('M',   'Male'),
                    ('F',   'Female'),
                   )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    sex = models.CharField(max_length=3, choices=SEX_CHOICES)
    nationality = models.CharField(max_length=128)
    
    date_registered = models.DateTimeField(default=datetime.now())
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)