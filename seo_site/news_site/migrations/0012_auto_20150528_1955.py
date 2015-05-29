# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0011_article_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description_text',
            field=models.TextField(),
        ),
    ]
