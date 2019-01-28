class Subject:
    def __init__(self, code, name, type, ects, schedules):
        self.code = code
        self.name = name
        self.type = type
        self.ects = ects
        self.schedules = schedules


def make_schedules(all_groups):
    schedules = {}
    all_groups = all_groups.replace("\n", "")
    all_groups = all_groups.replace("\r", "")
    groups = all_groups.split("@")
    for i in groups:
        group_sche = i.split(":")
        schedules[group_sche[0]] = group_sche[1]
    return schedules


def make_attributes():
    subjects = []
    with open("data.dat") as f:
        for line in f:
            splitter = line.split("@", 4)
            code = splitter[0]
            name = splitter[1]
            type = splitter[2]
            ects = splitter[3]
            schedules = make_schedules(splitter[4])
            subjects.append(Subject(code, name, type, ects, schedules))
    return subjects


