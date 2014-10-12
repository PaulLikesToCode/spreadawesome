# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0004_auto_20141012_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitterinfo',
            name='twitter_handle',
        ),
    ]
