# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0013_article_feed_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_ngrams',
            field=models.TextField(default=datetime.datetime(2015, 5, 29, 10, 3, 47, 924810, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='description_ngrams',
            field=models.TextField(default='coucou'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='lemmatized_description',
            field=models.TextField(default='coucou'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='lemmatized_text',
            field=models.TextField(default='coucou'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='tf_idf_description_words',
            field=models.TextField(default='coucou'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='tf_idf_text_words',
            field=models.TextField(default='coucou'),
            preserve_default=False,
        ),
    ]
