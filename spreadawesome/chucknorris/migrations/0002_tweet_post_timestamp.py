# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='post_timestamp',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
