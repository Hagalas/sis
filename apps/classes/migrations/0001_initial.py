# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150428_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Class Room')),
                ('location', models.CharField(max_length=100, verbose_name='Location', blank=True)),
            ],
            options={
                'verbose_name': 'Class Room',
                'verbose_name_plural': 'Class Rooms',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Class Subject',
                'verbose_name_plural': 'Class Subjects',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('klass', models.ForeignKey(related_name='class_years', verbose_name='Class', to='classes.Class')),
                ('lead_teacher', models.ForeignKey(related_name='teacher_classes', blank=True, to='users.UserProfile', null=True)),
                ('students', models.ManyToManyField(related_name='classes', null=True, to='users.UserProfile', blank=True)),
            ],
            options={
                'verbose_name': 'Class Year',
                'verbose_name_plural': 'Class Years',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.DecimalField(verbose_name='Grade', max_digits=4, decimal_places=2, choices=[(0, '0'), (1, '1'), (1.35, '1+'), (1.75, '2-'), (2, '2'), (2.35, '2+'), (2.75, '3-'), (3, '3'), (3.35, '3+'), (3.75, '4-'), (4, '4'), (4.35, '4+'), (4.75, '5-'), (5, '5'), (5.35, '5+'), (5.75, '6-'), (6, '6')])),
                ('weight', models.PositiveSmallIntegerField(default=1, verbose_name='Weight', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('notes', models.TextField(verbose_name='Notes', blank=True)),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GradeCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, verbose_name='Name')),
                ('weight', models.PositiveSmallIntegerField(verbose_name='Weight', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
            ],
            options={
                'verbose_name': 'Grade Category',
                'verbose_name_plural': 'Grade Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('subject', models.CharField(max_length=200, null=True, verbose_name='Lesson Subject', blank=True)),
                ('notes', models.TextField(verbose_name='Notes', blank=True)),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LessonAbsence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('excused', models.BooleanField(default=False, verbose_name='Excused')),
                ('notes', models.TextField(verbose_name='Notes', blank=True)),
                ('lesson', models.ForeignKey(related_name='absences', verbose_name='Lesson', to='classes.Lesson')),
                ('student', models.ForeignKey(related_name='absences', verbose_name='Student', to='users.UserProfile', null=True)),
            ],
            options={
                'verbose_name': 'Lesson Absence',
                'verbose_name_plural': 'Lessons Absences',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('starts_at', models.DateField(verbose_name='Starts at')),
                ('ends_at', models.DateField(verbose_name='Ends at')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('starts_at', models.DateField(verbose_name='Starts at')),
                ('ends_at', models.DateField(verbose_name='Ends at')),
            ],
            options={
                'verbose_name': 'School Year',
                'verbose_name_plural': 'School Years',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('teachers', models.ManyToManyField(to='users.UserProfile', blank=True)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubjectScheduleDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.PositiveSmallIntegerField(default=0, verbose_name='Day', choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('hours', models.PositiveSmallIntegerField(default=1, verbose_name='Hours')),
                ('starts_at', models.TimeField(verbose_name='Starts at')),
                ('ends_at', models.TimeField(verbose_name='Ends at')),
                ('classroom', models.ForeignKey(blank=True, to='classes.ClassRoom', null=True)),
                ('klass', models.ForeignKey(verbose_name='Class', to='classes.ClassYear')),
                ('schedule', models.ForeignKey(related_name='scheduled_subjects', to='classes.Schedule')),
                ('subject', models.ForeignKey(verbose_name='Subject', to='classes.Subject')),
                ('teacher', models.ForeignKey(related_name='+', verbose_name='Teacher', to='users.UserProfile', null=True)),
            ],
            options={
                'ordering': ('day', 'starts_at'),
                'verbose_name': 'Subject Schedule',
                'verbose_name_plural': 'Subject Schedules',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='schedule',
            name='year',
            field=models.ForeignKey(related_name='schedules', verbose_name='School Year', to='classes.SchoolYear', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='schedule',
            field=models.ForeignKey(verbose_name='Schedule', to='classes.SubjectScheduleDate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grade',
            name='category',
            field=models.ForeignKey(blank=True, to='classes.GradeCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grade',
            name='lesson',
            field=models.ForeignKey(to='classes.Lesson', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(related_name='grades', verbose_name='Student', to='users.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grade',
            name='teacher',
            field=models.ForeignKey(related_name='+', verbose_name='Teacher', to='users.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classyear',
            name='year',
            field=models.ForeignKey(verbose_name='School Year', to='classes.SchoolYear'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classsubject',
            name='klass',
            field=models.ForeignKey(related_name='subjects', verbose_name='Class', to='classes.ClassYear'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classsubject',
            name='subject',
            field=models.ForeignKey(verbose_name='Subject', to='classes.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classsubject',
            name='teachers',
            field=models.ManyToManyField(to='users.UserProfile', blank=True),
            preserve_default=True,
        ),
    ]
