# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_text', models.CharField(max_length=200)),
                ('description_text', models.CharField(max_length=200)),
                ('content_text', models.TextField()),
                ('public_date', models.DateTimeField(verbose_name=b'date published')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
