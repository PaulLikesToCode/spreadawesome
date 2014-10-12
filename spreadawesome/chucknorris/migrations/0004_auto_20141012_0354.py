# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0003_auto_20141011_0527'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterinfo',
            name='oauth_secret',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='twitterinfo',
            name='oauth_token',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='twitterinfo',
            name='twitter_handle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
