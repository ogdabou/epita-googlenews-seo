# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0012_auto_20150528_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='feed_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
