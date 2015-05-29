# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0014_auto_20150529_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='keywords',
            field=models.TextField(default=[]),
            preserve_default=False,
        ),
    ]
