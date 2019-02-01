from django.contrib import admin
from .models import Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "type", "semester", "ects"]
    ordering = ["code"]


admin.site.register(Subject, SubjectAdmin)
