# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0004_article_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='public_date',
            field=models.DateTimeField(verbose_name=b'date published', blank=True),
        ),
    ]
