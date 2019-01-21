from django.shortcuts import render


def select_subjects(request):
    print(request.POST.get("subject_name"))
    
    return render(request, "ScheduleGenerator/SelectSubjects.html")


def homepage(request):
    return render(request, "ScheduleGenerator/homepage.html")


def about(request):
    return render(request, "ScheduleGenerator/about.html")
