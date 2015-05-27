__author__ = 'ogdabou'

from django.contrib.admin.helpers import ActionForm
from django.db import models

class FeedForm(ActionForm):
    lolol = models.CharField(max_length=200)
