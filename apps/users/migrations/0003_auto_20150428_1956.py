# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150428_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='signature',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='signature_upload',
            field=models.ImageField(default='', upload_to=b'signatures'),
            preserve_default=False,
        ),
    ]
