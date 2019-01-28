class DataObject:
    def __init__(self):
        self.code = None
        self.name = None
        self.type = None
        self.ects = None
        self.schedules = {}

    def make_schedules(self, all_groups):
        all_groups = all_groups.replace("\n", "")
        all_groups = all_groups.replace("\r", "")
        groups = all_groups.split("@")
        for i in groups:
            group_sche = i.split(":")
            self.schedules[group_sche[0]] = group_sche[1]

    def make_attributes(self):
        with open("data.dat") as f:
            for line in f:
                splitter = line.split("@", 4)
        self.code = splitter[0]
        self.name = splitter[1]
        self.type = splitter[2]
        self.ects = splitter[3]
        self.make_schedules(splitter[4])

'''
if __name__ == "__main__":
    do = DataObject()
    do.make_attributes()
    print(do.name)'''
