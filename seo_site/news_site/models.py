from django.db import models
#from django.utils import timezone
from datetime import datetime


# Create your models here.

class Article(models.Model):
    url = models.TextField();
    title_text = models.CharField(max_length=200);
    description_text = models.CharField(max_length=200);
    content_text = models.TextField();
    public_date = models.DateTimeField('date published', default=datetime.now, blank=True);
    img_url = models.TextField(blank=True);
    
    def __str__(self):              
        return self.title_text

class Feed(models.Model):
    url = models.CharField(max_length=200)
