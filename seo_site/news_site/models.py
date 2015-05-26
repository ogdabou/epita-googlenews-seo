from django.db import models
from django.template.defaultfilters import default

# Create your models here.

class Article(models.Model):
    title_text = models.CharField(max_length=200);
    description_text = models.CharField(max_length=200);
    content_text = models.TextField();
    public_date = models.DateTimeField('date published');

