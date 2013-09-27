from django.db import models
import datetime
from django.utils import timezone

class Post(models.Model):
    post = models.CharField(max_length=5000)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):  # Python 3: def __str__(self):
            return self.post
    
    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
            
class Comment(models.Model):
    email = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    text = models.CharField(max_length=10000)
    post_id = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.text