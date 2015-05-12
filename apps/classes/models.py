from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

from django.db import models


@python_2_unicode_compatible
class SchoolYear(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    starts_at = models.DateField(_('Starts at'))
    ends_at = models.DateField(_('Ends at'))

    def __str__(self):
        return self.name

    def is_active(self):
        return self.starts_at <= now() <= self.ends_at

    class Meta:
        verbose_name = _('School Year')
        verbose_name_plural = _('School Years')


@python_2_unicode_compatible
class Subject(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    teachers = models.ManyToManyField('users.UserProfile', blank=True, limit_choices_to={'is_teacher': True})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')


@python_2_unicode_compatible
class Class(models.Model):
    description = models.TextField(_('Description'))

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('Class')
        verbose_name_plural = _('Classes')


@python_2_unicode_compatible
class ClassYear(models.Model):
    name = models.CharField(_('Name'), max_length=40)
    klass = models.ForeignKey(Class, verbose_name=_('Class'), related_name='class_years')
    year = models.ForeignKey(SchoolYear, verbose_name=_('School Year'))
    lead_teacher = models.ForeignKey('users.UserProfile', blank=True, null=True, limit_choices_to={'is_teacher': True},
                                     related_name='teacher_classes')
    students = models.ManyToManyField('users.UserProfile', blank=True, null=True, limit_choices_to={'is_student': True},
                                      related_name='classes')

    def __str__(self):
        return '%s (%s)' % (self.name, self.year)

    class Meta:
        verbose_name = _('Class Year')
        verbose_name_plural = _('Class Years')


@python_2_unicode_compatible
class ClassSubject(models.Model):
    subject = models.ForeignKey(Subject, verbose_name=_('Subject'))
    klass = models.ForeignKey(ClassYear, verbose_name=_('Class'), related_name='subjects')
    teachers = models.ManyToManyField('users.UserProfile', blank=True, limit_choices_to={'is_teacher': True})

    def __str__(self):
        return '%s: %s' % (self.subject, self.klass)

    class Meta:
        verbose_name = _('Class Subject')
        verbose_name_plural = _('Class Subjects')


@python_2_unicode_compatible
class ClassRoom(models.Model):
    name = models.CharField(_('Class Room'), max_length=100)
    location = models.CharField(_('Location'), max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Class Room')
        verbose_name_plural = _('Class Rooms')


@python_2_unicode_compatible
class Schedule(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    starts_at = models.DateField(_('Starts at'))
    ends_at = models.DateField(_('Ends at'))
    year = models.ForeignKey(SchoolYear, verbose_name=_('School Year'), null=True, related_name='schedules')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Schedule')
        verbose_name_plural = _('Schedules')


@python_2_unicode_compatible
class SubjectScheduleDate(models.Model):
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)
    DAYS = (
        (MONDAY, _('Monday')),
        (TUESDAY, _('Tuesday')),
        (WEDNESDAY, _('Wednesday')),
        (THURSDAY, _('Thursday')),
        (FRIDAY, _('Friday')),
        (SATURDAY, _('Saturday')),
        (SUNDAY, _('Sunday')),
    )

    schedule = models.ForeignKey(Schedule, related_name='scheduled_subjects')
    klass = models.ForeignKey(ClassYear, verbose_name=_('Class'))
    subject = models.ForeignKey(Subject, verbose_name=_('Subject'))
    teacher = models.ForeignKey('users.UserProfile', verbose_name=_('Teacher'), related_name='+', null=True)
    classroom = models.ForeignKey(ClassRoom, blank=True, null=True)

    day = models.PositiveSmallIntegerField(_('Day'), choices=DAYS, default=MONDAY)
    hours = models.PositiveSmallIntegerField(_('Hours'), default=1)
    starts_at = models.TimeField(_('Starts at'))
    ends_at = models.TimeField(_('Ends at'))

    def __str__(self):
        return '%s, %s (%s, %s-%s)' % (self.subject, self.klass, self.get_day_display() if self.day is not None else '?',
                                       self.starts_at, self.ends_at)

    def is_active(self):
        return self.starts_at <= now() <= self.ends_at

    class Meta:
        verbose_name = _('Subject Schedule')
        verbose_name_plural = _('Subject Schedules')
        ordering = ('day', 'starts_at')


@python_2_unicode_compatible
class Lesson(models.Model):
    schedule = models.ForeignKey(SubjectScheduleDate, verbose_name=_('Schedule'))
    date = models.DateField(_('Date'), default=now)
    subject = models.CharField(_('Lesson Subject'), max_length=200, blank=True, null=True)
    notes = models.TextField(_('Notes'), blank=True)

    def __str__(self):
        return '%s @ %s' % (self.schedule, self.date)

    def absent_ids(self):
        return list(self.absences.all().values_list('student_id', flat=True))

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')


@python_2_unicode_compatible
class LessonAbsence(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=_('Lesson'), related_name='absences')
    student = models.ForeignKey('users.UserProfile', verbose_name=_('Student'), related_name='absences',
                                limit_choices_to={'is_student': True}, null=True)
    excused = models.BooleanField(_('Excused'), default=False)
    notes = models.TextField(_('Notes'), blank=True)

    def __str__(self):
        return '%s' % self.lesson

    class Meta:
        verbose_name = _('Lesson Absence')
        verbose_name_plural = _('Lessons Absences')


@python_2_unicode_compatible
class GradeCategory(models.Model):
    name = models.CharField(_('Name'), max_length=1000)
    weight = models.PositiveSmallIntegerField(_('Weight'), choices=[(i, i) for i in range(1, 10)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Grade Category')
        verbose_name_plural = _('Grade Categories')


@python_2_unicode_compatible
class Grade(models.Model):
    GRADES = (
        (0, '0'),
        (1, '1'),
        (1.35, '1+'),
        (1.75, '2-'),
        (2, '2'),
        (2.35, '2+'),
        (2.75, '3-'),
        (3, '3'),
        (3.35, '3+'),
        (3.75, '4-'),
        (4, '4'),
        (4.35, '4+'),
        (4.75, '5-'),
        (5, '5'),
        (5.35, '5+'),
        (5.75, '6-'),
        (6, '6'),
    )

    student = models.ForeignKey('users.UserProfile', verbose_name=_('Student'), related_name='grades',
                                limit_choices_to={'is_student': True})
    teacher = models.ForeignKey('users.UserProfile', verbose_name=_('Teacher'), related_name='+',
                                limit_choices_to={'is_teacher': True})
    lesson = models.ForeignKey(Lesson, null=True)
    grade = models.DecimalField(_('Grade'), max_digits=4, decimal_places=2, choices=GRADES)
    weight = models.PositiveSmallIntegerField(_('Weight'), choices=[(i, i) for i in range(1, 10)], default=1)
    category = models.ForeignKey(GradeCategory, null=True, blank=True)
    notes = models.TextField(_('Notes'), blank=True)

    def __str__(self):
        return '%s' % self.grade

    class Meta:
        verbose_name = _('Grade')
        verbose_name_plural = _('Grades')