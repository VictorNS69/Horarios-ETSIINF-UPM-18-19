from django.shortcuts import render


def select_subjects(request):
    print(request.POST.get("inlineRadioOptions"))

    return render(request, "ScheduleGenerator/select_course.html")


def homepage(request):
    return render(request, "ScheduleGenerator/homepage.html")


def about(request):
    return render(request, "ScheduleGenerator/about.html")
