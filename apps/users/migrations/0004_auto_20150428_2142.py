# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150428_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='genders',
            field=models.CharField(verbose_name='Gender', max_length=10, default='male', choices=[('male', 'Male'), ('female', 'Female')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='signature_upload',
            field=models.ImageField(blank=True, upload_to='signatures', null=True),
        ),
    ]
