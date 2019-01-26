from django.db import models
from django.core.validators import MinValueValidator
from multiselectfield import MultiSelectField


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.BigIntegerField(primary_key=True)
    ects = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(1)])
    TYPES = (
        ("Basica", "Basica"), ("Obligatoria", "Obligatoria"), ("Opcional", "Opcional")
    )
    type = models.CharField(choices=TYPES, blank=False, max_length=10)
    SEMESTERS = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8))
    semester = MultiSelectField(choices=SEMESTERS, blank=False)
    # Dictionary with the form schedules = { "1M":("L09-10", "M11-12") ... }
    # If the group does not exist in the dictionary, this means that the subjects is not related with the group
    schedules = models.TextField(blank=False)

    '''
    GROUPS = (
        # First and second semester
        ("1M", "1M"), ("2M", "2M"), ("2M-B", "2M-B"), ("3M", "3M"), ("3M-B", "3M-B"),
        # Third semester
        ("3S1M", "3S1M"), ("3S1M-B", "3S1M-B"), ("3S2M", "3S2M"), ("3S2M-B", "3S2M-B"), ("3S3T", "3S3T"),
        # Forth semester
        ("4S1M", "4S1M"), ("4S1M-B", "4S1M-B"), ("4S2M", "4S2M"), ("4S2M-B", "4S2M-B"), ("4S3T", "4S3T"),
        # Fifth semester
        ("5S1M", "5S1M"), ("5S2M", "5S2M"), ("5S3T", "5S3T"),
        # Sixth semester
        ("6S1M", "6S1M"), ("6S2M", "6S2M"), ("6S3T", "6S3T"),
        # Seventh semester
        ("7S1T", "7S1T"), ("7S1T-B", "7S1T-B"),
        # Eighth semester
        ("8S1T", "8S1T"), ("8S1T-B", "8S1T-B"),
    )
    SCHEDULES = (
        ("L9-10", "L9-10"), ("L10-11", "L10-11"), ("L11-12", "L11-12"), ("L12-13", "L12-13"), ("L13-14", "L13-14"),
        ("L14-15", "L14-15"), ("L15-16", "L15-16"), ("L16-17", "L16-17"), ("L17-18", "L17-18"), ("L18-19", "L18-19"),
        ("L19-20", "L19-20"), ("L20-21", "L20-21"), ("M9-10", "M9-10"), ("M10-11", "M10-11"), ("M11-12", "M11-12"),
        ("M12-13", "M12-13"), ("M13-14", "M13-14"), ("M14-15", "M14-15"), ("M15-16", "M15-16"), ("M16-17", "M16-17"),
        ("M17-18", "M17-18"), ("M18-19", "M18-19"), ("M19-20", "M19-20"), ("M20-21", "M20-21"), ("MI9-10", "MI9-10"),
        ("MI10-11", "MI10-11"), ("MI11-12", "MI11-12"), ("MI12-13", "MI12-13"), ("MI13-14", "MI13-14"),
        ("MI14-15", "MI14-15"), ("MI15-16", "MI15-16"), ("MI16-17", "MI16-17"), ("MI17-18", "MI17-18"),
        ("MI18-19", "MI18-19"), ("MI19-20", "MI19-20"), ("MI20-21", "MI20-21"), ("J9-10", "J9-10"),
        ("J10-11", "J10-11"), ("J11-12", "J11-12"), ("J12-13", "J12-13"), ("J13-14", "J13-14"), ("J14-15", "J14-15"),
        ("J15-16", "J15-16"), ("J16-17", "J16-17"), ("J17-18", "J17-18"), ("J18-19", "J18-19"), ("J19-20", "J19-20"),
        ("J20-21", "J20-21"), ("V9-10", "V9-10"), ("V10-11", "V10-11"), ("V11-12", "V11-12"), ("V12-13", "V12-13"),
        ("V13-14", "V13-14"), ("V14-15", "V14-15"), ("V15-16", "V15-16"), ("V16-17", "V16-17"), ("V17-18", "V17-18"),
        ("V18-19", "V18-19"), ("V19-20", "V19-20"), ("V20-21", "V20-21")
    )
    groups = MultiSelectField(
        choices=GROUPS, blank=False)
    schedules = MultiSelectField(
        choices=SCHEDULES, blank=False)
    '''

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
