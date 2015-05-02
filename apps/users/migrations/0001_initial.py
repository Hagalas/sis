# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name', blank=True)),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name', blank=True)),
                ('phone', models.CharField(max_length=100, verbose_name='Phone Number', blank=True)),
                ('email', models.EmailField(max_length=100, verbose_name='Email', blank=True)),
                ('date_of_birth', models.DateField(null=True, verbose_name='Date of birth', blank=True)),
                ('genders', models.CharField(default=b'male', max_length=10, verbose_name='Gender', choices=[(b'male', 'Male'), (b'female', 'Female')])),
                ('pesel', models.CharField(max_length=11, null=True, verbose_name='PESEL', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_parent', models.BooleanField(default=False, verbose_name='Is parent')),
                ('is_student', models.BooleanField(default=False, verbose_name='Is student')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Is teacher')),
                ('user', models.OneToOneField(related_name='profile', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
            bases=(models.Model,),
        ),
    ]
