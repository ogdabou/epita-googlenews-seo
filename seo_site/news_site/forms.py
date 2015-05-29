__author__ = 'ogdabou'

from django.contrib.admin.helpers import ActionForm
from django.db import models
from django import forms

class FeedForm(ActionForm):
    lolol = models.CharField(max_length=200)

class RequestForm(ActionForm):
    bla = models.CharField(max_length=50)