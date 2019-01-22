from django.shortcuts import render


def select_course(request):
    if request.POST.get("inlineRadioOptions") == "1":
        return render(request, 'ScheduleGenerator/select_subjects.html', {'courts': "c", 'club_name': "club_name"})
    # TODO add the other courses
    return render(request, "ScheduleGenerator/select_course.html")


def homepage(request):
    return render(request, "ScheduleGenerator/homepage.html")


def about(request):
    return render(request, "ScheduleGenerator/about.html")


def select_subjects(request):
    return render(request, "ScheduleGenerator/select_subjects.html")
