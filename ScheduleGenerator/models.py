from django.db import models
from django.core.validators import MinValueValidator
from multiselectfield import MultiSelectField


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.BigIntegerField(primary_key=True)
    ects = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(1)])
    TYPES = (
        ("BASICA", "BASICA"), ("OBLIGATORIA", "OBLIGATORIA"), ("OPCIONAL", "OPCIONAL")
    )
    type = models.CharField(choices=TYPES, blank=False, max_length=10)
    SEMESTERS = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8))
    semester = MultiSelectField(choices=SEMESTERS, blank=False)
    # Dictionary with the form schedules = { "1M":("L09-10", "M11-12") ... }
    # If the group does not exist in the dictionary, this means that the subjects is not related with the group
    schedules = models.TextField(blank=False)

    '''
    Transforms the self.schedules TextField into a Dictionary if the TextField is well written
    '''
    def get_schedules(self):
        schedules = {}
        try:
            for line in str(self.schedules).splitlines():
                s = line.split(":")
                schedules[s[0]] = s[1][:-2]

        except Exception:
            print("ERROR: Could not import schedules for " + str(self.name))
            return "ERROR: Could not import schedules for " + str(self.name)

        return schedules

    def __str__(self):
        return str(self.code) + ": " + str(self.name)

    '''
    Prints all the subject attributes 
    '''
    def info(self):
        schedules = self.get_schedules()
        return "Name: " + str(self.name) + "\nCode: " + str(self.code) + "\nECTS: " + str(self.ects) + "\nType: " \
               + str(self.type) + "\nSemester: " + str(self.semester) + "\nSchedules: " + str(schedules)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
