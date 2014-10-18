# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chucknorris', '0007_auto_20141017_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='quote_id',
            field=models.ForeignKey(blank=True, to='chucknorris.Quote', null=True),
        ),
    ]
