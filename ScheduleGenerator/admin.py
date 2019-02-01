from django.contrib import admin
from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "type", "semester", "ects"]
    ordering = ["code"]
    list_filter = ("type", "semester", "ects")


admin.site.register(Subject, SubjectAdmin)
