from django.db import models
import datetime
from django.utils import timezone

class Bio(models.Model):
    about = models.CharField(max_length=2000, blank=True)
    city = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=50, blank=True)
    company_site = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=40)
    fname = models.CharField(max_length=20)
    github = models.CharField(max_length=100, blank=True)
    languages = models.CharField(max_length=400, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    lname = models.CharField(max_length=20)
    major = models.CharField(max_length=75, blank=True)
    minor = models.CharField(max_length=75, blank=True)
    site1_name = models.CharField(max_length=100, blank=True)
    site1_url = models.CharField(max_length=100, blank=True)
    site2_name = models.CharField(max_length=100, blank=True)
    site2_url = models.CharField(max_length=100, blank=True)
    site3_name = models.CharField(max_length=100, blank=True)
    site3_url = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=400, blank=True)
    state = models.CharField(max_length=10, blank=True)
    technologies = models.CharField(max_length=400, blank=True)
    title = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    
    def __unicode__(self):  # Python 3: def __str__(self):
            return self.about