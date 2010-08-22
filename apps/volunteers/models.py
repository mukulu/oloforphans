from datetime import datetime

from django.db import models
from django.conf import settings

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
    middle_name = models.CharField(null=True,blank=True,max_length=128)
    last_name = models.CharField(max_length=128,help_text="Volunteer's last or surname")
    e_mail = models.EmailField(null=True,blank=True,max_length=128,help_text="Volunteer's E-mail address")
    photo = models.ImageField(null=True,blank=True,upload_to=settings.PHOTO_DIR, help_text="Recent Photo")
    sex = models.CharField(max_length=3, choices=SEX_CHOICES)
    nationality = models.CharField(max_length=128)
    occupation = models.CharField(null=True,blank=True,max_length=128,help_text="Volunteer's job or profession")
    
    date_registered = models.DateTimeField(default = datetime.now(),auto_now=True)
    
    class Meta:
        ordering = ['-date_registered']
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
