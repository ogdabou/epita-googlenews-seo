# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0002_feed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='content_text',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='description_text',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='public_date',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='title_text',
        ),
    ]
