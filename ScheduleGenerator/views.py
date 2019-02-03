from django.shortcuts import render
from .models import Subject
from .algorithm import schedule_generator_algorithm


def select_course(request):
    subjects = Subject.objects.none()
    if '1º' in request.GET:
        f1 = Subject.objects.filter(semester="1")
        f2 = Subject.objects.filter(semester="2")
        union = f1.union(f2)
        subjects = subjects.union(union)

    if '2º' in request.GET:
        f1 = Subject.objects.filter(semester="3")
        f2 = Subject.objects.filter(semester="4")
        union = f1.union(f2)
        subjects = subjects.union(union)

    if '3º' in request.GET:
        f1 = Subject.objects.filter(semester="5")
        f2 = Subject.objects.filter(semester="6")
        union = f1.union(f2)
        subjects = subjects.union(union)

    if '4º' in request.GET:
        f1 = Subject.objects.filter(semester="7")
        f2 = Subject.objects.filter(semester="8")
        union = f1.union(f2)
        subjects = subjects.union(union)

    if 'Optional' in request.GET:
        f = Subject.objects.filter(type="Optional")
        subjects = subjects.union(f)

    if request.GET.get("Continue"):
        return select_subjects(request, subjects.order_by("semester"))

    return render(request, "ScheduleGenerator/select_course.html")


def homepage(request):
    return render(request, "ScheduleGenerator/homepage.html")


def about(request):
    return render(request, "ScheduleGenerator/about.html")


def select_subjects(request, context):
    print("in select_subjects")
    schedule_generator_algorithm(context)
    return render(request, "ScheduleGenerator/select_subjects.html", {'context': context})
