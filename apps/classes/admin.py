from __future__ import unicode_literals

from django.contrib import admin
from core.admin import BaseModelAdmin

from django.utils.translation import ugettext_lazy as _, ugettext
from core.utils import admin_url, register_list_field

from .models import (SchoolYear, Subject, Class, ClassYear, ClassSubject, Schedule, SubjectScheduleDate, ClassRoom,
                     Lesson, LessonAbsence, GradeCategory, Grade)


class SchoolYearAdmin(BaseModelAdmin):
    list_display = ('name', 'starts_at', 'ends_at', '_schedules', '_actions')

    def _actions(self, obj):
        actions = []
        actions.append('<a href="%s?year__id__exact=%s">%s</a>' % (admin_url('classes', 'schedule', 'changelist'),
                                                                    obj.id, ugettext('Schedules')))
        actions.append('<a href="%s?year__id__exact=%s">%s</a>' % (admin_url('classes', 'classyear', 'changelist'),
                                                                    obj.id, ugettext('Class Years')))
        return ' | '.join(actions)
    _actions.short_description = _('Actions')
    _actions.allow_tags = True


register_list_field(SchoolYearAdmin, '_schedules', _('Schedules'),
                    func=lambda obj: (admin_url('classes', 'schedule', 'change', args=(obj.id,)), obj),
                    qs_func=lambda obj: obj.schedules.all().order_by('starts_at'))


class SubjectAdmin(BaseModelAdmin):
    list_display = ('name', '_teachers')


register_list_field(SubjectAdmin, '_teachers', _('Teachers'),
                    func=lambda obj: (admin_url('users', 'userprofile', 'change', args=(obj.id,)), obj),
                    qs_func=lambda obj: obj.teachers.all())


class ClassAdmin(BaseModelAdmin):
    list_display = ('description', '_years', '_actions')

    def _actions(self, obj):
        actions = []
        actions.append('<a href="%s?klass__id__exact=%s">%s</a>' % (admin_url('classes', 'classyear', 'changelist'),
                                                                    obj.id, ugettext('Show Class Years')))
        return ' | '.join(actions)
    _actions.short_description = _('Actions')
    _actions.allow_tags = True


register_list_field(ClassAdmin, '_years', _('Class Years'),
                    func=lambda obj: (admin_url('classes', 'classyear', 'change', args=(obj.id,)), obj),
                    qs_func=lambda obj: obj.class_years.all())


class ClassYearAdmin(BaseModelAdmin):
    list_display = ('name', 'year', '_students', '_actions')
    list_filter = ('year',)

    def _actions(self, obj):
        actions = []
        actions.append('<a href="%s?klass__id__exact=%s">%s</a>' % (admin_url('classes', 'classsubject', 'changelist'),
                                                                    obj.id, ugettext('Show Subjects')))
        return ' | '.join(actions)
    _actions.short_description = _('Actions')
    _actions.allow_tags = True


register_list_field(ClassYearAdmin, '_students', _('Students'),
                    func=lambda obj: (admin_url('users', 'userprofile', 'change', args=(obj.id,)), obj),
                    qs_func=lambda obj: obj.students.all())


class ClassSubjectAdmin(BaseModelAdmin):
    list_display = ('subject', 'klass', '_teachers')
    list_filter = ('subject', 'klass',)


register_list_field(ClassSubjectAdmin, '_teachers', _('Teachers'),
                    func=lambda obj: (admin_url('users', 'userprofile', 'change', args=(obj.id,)), obj),
                    qs_func=lambda obj: obj.teachers.all())


class ScheduleAdmin(BaseModelAdmin):
    list_display = ('name', 'year', 'starts_at', 'ends_at')
    list_filter = ('year',)


class SubjectScheduleDateAdmin(BaseModelAdmin):
    list_display = ('schedule', 'day', '_time', '_subject', 'klass', 'teacher')
    list_filter = ('subject', 'klass', 'schedule', 'day')

    def _time(self, obj):
        return '%s-%s' % (obj.starts_at, obj.ends_at)
    _time.short_description = _('Time')

    def _subject(self, obj):
        if obj.classroom:
            return '%s (%s)' % (obj.subject, obj.classroom)
        return obj.subject
    _subject.short_description = _('Subject')


class GradeCategoryAdmin(BaseModelAdmin):
    list_display = ('name', 'weight')


class GradeAdmin(BaseModelAdmin):
    list_display = ('lesson', 'grade')


class LessonAbsenceInline(admin.TabularInline):
    model = LessonAbsence
    extra = 1


class LessonAdmin(BaseModelAdmin):
    list_filter = ('date', 'schedule__subject')
    list_display = ('date', 'schedule', 'subject')
    inlines = [LessonAbsenceInline]


admin.site.register(Subject, SubjectAdmin)
admin.site.register(SchoolYear, SchoolYearAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(ClassYear, ClassYearAdmin)
admin.site.register(ClassSubject, ClassSubjectAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(SubjectScheduleDate, SubjectScheduleDateAdmin)
admin.site.register(ClassRoom)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(GradeCategory, GradeCategoryAdmin)
admin.site.register(Grade, GradeAdmin)