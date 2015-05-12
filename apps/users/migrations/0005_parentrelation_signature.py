# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150428_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentrelation',
            name='signature',
            field=models.CharField(max_length=255, null=True, verbose_name='sig', blank=True),
            preserve_default=True,
        ),
    ]
