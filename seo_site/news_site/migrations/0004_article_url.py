# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0003_auto_20150527_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
