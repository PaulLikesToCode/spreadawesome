# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0013_auto_20141017_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='post_timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
