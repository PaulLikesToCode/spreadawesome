# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0008_auto_20141017_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='post_timestamp',
            field=models.DateTimeField(),
        ),
    ]
