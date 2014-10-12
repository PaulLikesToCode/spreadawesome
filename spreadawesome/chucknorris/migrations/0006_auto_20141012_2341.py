# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0005_remove_twitterinfo_twitter_handle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='receipent_handle',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
