# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0015_feed_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='keywords',
            field=models.TextField(blank=True),
        ),
    ]
