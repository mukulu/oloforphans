from django.db import models

class Subject(models.Model):
    '''
        The studies been taught in school.
        eg. Mathematics, Physics,... etc.
    '''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True,blank=True,\
                                   help_text="About the subject.")
    
    def __unicode__(self):
        return self.name

class SchoolClass(models.Model):
    '''
        A Class of student, in accordance to forms.
    '''
    name = models.CharField(max_length=128, unique=True, help_text='name of the class')
    subjects = models.ManyToManyField('Subject')
    
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
    
    def __unicode__(self):
        return self.name
    

