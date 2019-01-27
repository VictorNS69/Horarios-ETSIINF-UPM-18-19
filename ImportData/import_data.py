

class ImportData:
    def __init__(self):


    def make_schedules(self, all_groups):
        self.schedules = {}
        with open("data.dat") as f:
            for line in f:
                groups = line.split("@")
                for i in groups:
                    group_sche = i.split(":")
                    if "\n" in group_sche:
                        groups[2].replace("\n", "")
                    self.schedules[group_sche[0]] = group_sche[1]

    def make_attributes(self):
        with open("data.dat") as f:
            for line in f:


'''
##  105000001@FUNDAMENTOS FISICOS Y TECNOLOGICOS DE LA INFORMATICA@Basica@6@
'''