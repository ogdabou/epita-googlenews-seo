from django.db import models
#from django.utils import timezone
from datetime import datetime


# Create your models here.

class Article(models.Model):
    url = models.TextField()
    title_text = models.CharField(max_length=200)
    description_text = models.TextField()
    lemmatized_description = models.TextField()
    lemmatized_text = models.TextField()
    description_ngrams = models.TextField()
    content_ngrams = models.TextField()
    tf_idf_description_words = models.TextField()
    tf_idf_text_words = models.TextField()
    content_text = models.TextField()
    public_date = models.DateTimeField('date published', default=datetime.now, blank=True)
    img_url = models.TextField(blank=True)
    feed_id = models.IntegerField()
    
    def __str__(self):              
        return self.title_text

class Feed(models.Model):
    url = models.CharField(max_length=200)
