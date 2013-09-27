from django.db import models
import datetime
from django.utils import timezone

class Paper(models.Model):
    authors = models.CharField(max_length=500, blank=True)
    descr = models.CharField(max_length=5000, blank=True)
    keywords = models.CharField(max_length=500, blank=True)
    news = models.CharField(max_length=5000, blank=True)
    awards = models.CharField(max_length=1000, blank=True)
    title = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=130, blank=True)
    
    def __unicode__(self):
            return self.post
    
