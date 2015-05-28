# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0010_auto_20150527_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img_url',
            field=models.TextField(blank=True),
        ),
    ]
