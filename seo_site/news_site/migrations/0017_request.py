# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0016_auto_20150529_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request', models.CharField(max_length=50)),
                ('corrected_request', models.CharField(max_length=50, blank=True)),
                ('results', models.TextField(blank=True)),
            ],
        ),
    ]
