from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField


class Semester (models.Model):
    # Grupos depende del semestre
    # Los horarios dependen del grupo
    semester = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(8), MinValueValidator(1)], unique=True)

    def __str__(self):
        return str(self.semester)


class Subject (models.Model):
    name = models.CharField(max_length=100)
    code = models.BigIntegerField(primary_key=True)
    ects = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(1)])
    type = models.CharField(max_length=20)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    GROUPS = (
        ("G1M", "G1M"),
        ("G2M", "G2M"),
        ("G2M-B", "G2M-B"),
        ("G3M", "G3M"),
        ("G3M-B", "G3M-B"),
        ("G3S1M", "G3S1M"),
        ("G3S1M-B", "G3S1M-B"),
        # This is not all the groups
    )
    SCHEDULES = (
        ("L9-10", "L9-10"),
        ("L10-11", "L10-11"),
        ("L11-12", "L11-12"),
        ("L12-13", "L12-13"),
        ("L13-14", "L13-14"),
        ("L14-15", "L14-15"),
        ("L15-16", "L15-16"),
        ("L16-17", "L16-17"),
        ("L17-18", "L17-18"),
        ("L18-19", "L18-19"),
        ("L19-20", "L19-20"),
        ("L20-21", "L20-21"),
        # This is not all the schedule possibilities
    )
    groups = MultiSelectField(
        choices=GROUPS, blank=False)
    schedules = MultiSelectField(
        choices=SCHEDULES, blank=False)

    def __str__(self):
        return str(self.code) + ": " + str(self.name)


