class Subject:
    def __init__(self, code, name, type, ects, semester, schedules):
        """
        Constructor
        :param code: Code of the subject
        :param name: Name of the subject
        :param type: Type of the subject
        :param ects: ects of the subject
        :param semester: Semester of the subject
        :param schedules: Schedules of the subject
        """
        self.code = code
        self.name = name
        self.type = type
        self.ects = ects
        self.semester = semester
        self.schedules = schedules


def make_schedules(all_groups):
    """
    Transforms the schedules from raw data into a dictionary
    :param all_groups: All the GROUP-SCHEDULES available with raw format
    :return: A dictionary with k-v GROUP-SCHEDULES
    """
    schedules = {}
    all_groups = all_groups.replace("\n", "")
    all_groups = all_groups.replace("\r", "")
    groups = all_groups.split("@")
    for i in groups:
        group_sche = i.split(":")
        schedules[group_sche[0]] = group_sche[1]
    return schedules


def make_attributes():
    """
    Creates Subjects objects from the raw data
    :return: An array of Subjects
    """
    subjects = []
    with open("data.dat") as f:
        for line in f:
            splitter = line.split("@", 5)
            code = splitter[0]
            name = splitter[1]
            type = splitter[2]
            ects = splitter[3]
            semester = splitter[4]
            schedules = make_schedules(splitter[5])
            subjects.append(Subject(code, name, type, ects, semester, schedules))
    return subjects


