# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0002_tweet_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweet_text',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='quote_id',
            field=models.ForeignKey(to='chucknorris.Quote', null=True),
        ),
    ]
