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
    middle_name = models.CharField(null=True, blank=True, max_length=128)
    last_name = models.CharField(max_length=128, help_text="Volunteer's last or surname")
    address = models.TextField()
    residence = models.CharField(max_length=128, help_text="Country of residence")
    nationality = models.CharField(max_length=128)
    phone_number = models.CharField(null=True, blank=True, max_length=128,help_text="Volunteer's current phone number")
    email = models.EmailField(null=True, blank=True, max_length=128,help_text="Volunteer's E-mail address")
    #photo = models.ImageField(null=True, blank=True, upload_to=settings.PHOTO_DIR, help_text="Recent Photo")
    sex = models.CharField(max_length=3, choices=SEX_CHOICES)
    occupation = models.CharField(null=True, blank=True, max_length=128, help_text="Volunteer's job or profession")
    
    application_date = models.DateTimeField(default = datetime.now,auto_now=True)
    
    class Meta:
        ordering = ['-application_date']
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
    
class VolunteerProfile(models.Model):
    """
        Volunteer's profile.
        #use the help_text as the qns on the forms
    """
    volunteer = models.ForeignKey(Volunteer)
    volunteering_startdate = models.DateField(help_text='Ideal date to start volunteering at Bethsaida')
    volunteering_enddate = models.DateField(help_text='Ideal date to end volunteering at Bethsaida')
    preferred_weeks = models.IntegerField()
    flexibility = models.CharField(max_length=128,help_text='How flexible are you regarding these dates')
    volunteering_reasons = models.TextField(help_text='Reasons for wanting to volunteer')
    previous_education = models.TextField()
    previous_employment = models.TextField(help_text='Previous employment and work/travel')
    experience_overseas = models.TextField()
    personal_interest = models.TextField()
    future_plans = models.TextField()
    strengths = models.TextField(help_text='what are your strength (list)')
    weaknesses = models.TextField(help_text='what are your weaknesses (list)')
    good_volunteer = models.TextField(help_text='Why do you think you will make a good volunteer?')
    goals = models.TextField(help_text="Please indicate any aspirations and goals you would like to achieve while volunteering at Bethsaida")
    emergency_contact = models.TextField('Emergency contact details, (name, address, phone, e-mail, and relationship to the individual')
    referee = models.TextField()
    language_and_culture = models.BooleanField()
    medical_conditions = models.TextField(help_text='Please explain if you have any medical conditions')
    concerns = models.TextField(help_text="Any other information or concern")
    
    def __unicode__(self):
        f = self.volunteer
        s = self.volunteering_startdate
        e = self.volunteering_enddate
        return "%s starts: %s to %s" % (f, s, e)
    
    
    
