# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0012_tweet_quote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='post_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
