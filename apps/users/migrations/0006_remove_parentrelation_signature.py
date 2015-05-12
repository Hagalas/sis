# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_parentrelation_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parentrelation',
            name='signature',
        ),
    ]
