from django.db import models
#from django.utils import timezone
#from datetime import datetime

# Create your models here.

class Article(models.Model):
    title_text = models.CharField(max_length=200);
    description_text = models.CharField(max_length=200);
    content_text = models.TextField();
    public_date = models.DateTimeField('date published');
    
    def __str__(self):              
        return self.title_text
    
    