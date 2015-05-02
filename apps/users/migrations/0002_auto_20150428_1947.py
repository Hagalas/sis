# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('child', models.ForeignKey(related_name='parent_rel', verbose_name='Child', to='users.UserProfile')),
                ('parent', models.ForeignKey(related_name='children_rel', verbose_name='Parent', to='users.UserProfile')),
            ],
            options={
                'verbose_name': 'Parent Relation',
                'verbose_name_plural': 'Parent Relations',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='signature',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
