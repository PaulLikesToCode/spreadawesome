# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0011_remove_tweet_quote_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='quote_id',
            field=models.ForeignKey(blank=True, to='chucknorris.Quote', null=True),
            preserve_default=True,
        ),
    ]
