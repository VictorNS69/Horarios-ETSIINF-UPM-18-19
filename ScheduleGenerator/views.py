from django.shortcuts import render
from django.db import models
from .models import Subject


def select_course(request):
    if request.POST.get("inlineRadioOptions") == "1":
        subject =Subject.objects.all()
        return render(request, 'ScheduleGenerator/select_subjects.html', {'subjects': subject})
    # TODO add the other courses
    return render(request, "ScheduleGenerator/select_course.html")


def homepage(request):
    return render(request, "ScheduleGenerator/homepage.html")


def about(request):
    return render(request, "ScheduleGenerator/about.html")


def select_subjects(request):
    return render(request, "ScheduleGenerator/select_subjects.html")
