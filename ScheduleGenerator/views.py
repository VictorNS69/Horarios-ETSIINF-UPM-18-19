from django.shortcuts import render


def select_subjects(request):
    return render(request, "ScheduleGenerator/SelectSubjects.html")


def homepage(request):
    return render(request, "ScheduleGenerator/homepage.html")


def about(request):
    return render(request, "ScheduleGenerator/about.html")
