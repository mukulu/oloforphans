from django.forms import ModelForm
from apps.volunteers.models import Volunteer, VolunteerProfile

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        #exclude = ('longitude','latitude','modified','created','type','parent')

class VolunteerProfileForm(ModelForm):
    class Meta:
        model = VolunteerProfile