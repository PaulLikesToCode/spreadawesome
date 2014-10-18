# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0010_auto_20141017_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='quote_id',
        ),
    ]
