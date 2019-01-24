from django.shortcuts import render
from django.db import models
from .models import Subject


def select_course(request):
    if request.POST.get("1º"):
        f1 = Subject.objects.filter(semester="1")
        f2 = Subject.objects.filter(semester="2")
        subjects = f1.union(f2)
        return render(request, 'ScheduleGenerator/select_subjects.html', {'subjects': subjects})

    if request.POST.get("2º"):
        f1 = Subject.objects.filter(semester="3")
        f2 = Subject.objects.filter(semester="4")
        subjects = f1.union(f2)
        return render(request, 'ScheduleGenerator/select_subjects.html', {'subjects': subjects})

    if request.POST.get("3º"):
        f1 = Subject.objects.filter(semester="5")
        f2 = Subject.objects.filter(semester="6")
        subjects = f1.union(f2)
        return render(request, 'ScheduleGenerator/select_subjects.html', {'subjects': subjects})

    if request.POST.get("4º"):
        f1 = Subject.objects.filter(semester="7")
        f2 = Subject.objects.filter(semester="8")
        subjects = f1.union(f2)
        return render(request, 'ScheduleGenerator/select_subjects.html', {'subjects': subjects})

    if request.POST.get("Optionalº"):
        subjects = Subject.objects.filter(type="Optional")
        return render(request, 'ScheduleGenerator/select_subjects.html', {'subjects': subjects})

    return render(request, "ScheduleGenerator/select_course.html")


def homepage(request):
    return render(request, "ScheduleGenerator/homepage.html")


def about(request):
    return render(request, "ScheduleGenerator/about.html")


def select_subjects(request):
    return render(request, "ScheduleGenerator/select_subjects.html")
