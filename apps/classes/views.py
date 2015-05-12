from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm

from users.models import *
from .models import *


def schedule(request):
    schedule_id = request.GET.get('id', 0)
    class_year = ClassYear.objects.get(id=request.GET.get('class_year'))

    days = []
    for day, name in SubjectScheduleDate.DAYS:
        subjects = SubjectScheduleDate.objects.filter(day=day, klass=class_year, schedule_id=schedule_id)
        days.append({
            'subjects': subjects,
            'name': name
        })

    return render(request, 'schedule.html', {'days': days})


def grades(request):
    subject = ClassSubject.objects.get(id=request.GET.get('id'))
    student = UserProfile.objects.get(id=request.GET.get('student'))
    lessons = Lesson.objects.filter(schedule__subject=subject).order_by('-date')
    grades = Grade.objects.filter(student=student, lesson__schedule__subject=subject).order_by('-lesson__date')

    s = sum([grade.grade*grade.weight for grade in grades])
    n = sum([grade.weight for grade in grades])

    return render(request, 'grades.html', {
        'subject': subject,
        'student': student,
        'lessons': lessons,
        'grades': grades,
        'avg': s/n if n > 0 else '-'
    })


def student_view(request, id):
    student = UserProfile.objects.get(id=id)

    if not 'class_year' in request.GET:
        class_years = ClassYear.objects.filter(students__id=student.id)
        return render(request, 'student_years.html', {
            'student': student,
            'class_years': class_years,
        })
    else:
        class_year = ClassYear.objects.get(id=request.GET.get('class_year'))
        return render(request, 'student.html', {
            'student': student,
            'class_year': class_year,
        })


def parent_view(request):
    student_id = request.GET.get('student', None)
    if not student_id:
        students = [rel.child for rel in request.user.profile.children_rel.all()]
        return render(request, 'parent_index.html', {
            'students': students
        })
    else:
        return student_view(request, student_id)


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.user_cache)
    else:
        form = AuthenticationForm()

    user = request.user
    if user is not None and user.is_authenticated():
        if user.profile.is_parent:
            return parent_view(request)
        elif user.profile.is_student:
            return student_view(request, request.user.profile.id)

    return render(request, 'login.html', {'form': form})