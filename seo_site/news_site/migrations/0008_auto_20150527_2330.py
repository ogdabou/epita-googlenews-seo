# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0007_auto_20150527_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='public_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 23, 30, 57, 101540, tzinfo=utc), verbose_name=b'date published', blank=True),
        ),
    ]
