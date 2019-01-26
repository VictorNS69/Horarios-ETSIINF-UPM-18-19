

s = "1M:L09-10,M12-13,M13-14,V10-11,V11-12@2M:MI10-11,MI11-12,J09-10,V12-13,V13-14@2M-B:MI10-11,MI11-12,J09-10,V12-13,V13-14@3M:L10-11,L11-12,M09-10,MI12-13,MI13-14"
schedules = {}

with open("../data.dat") as f:
    for line in f:
        aux = line.split("@")
        # print(aux)
        for i in aux:
            aux2 = i.split(":")
            if "\n" in aux2:
                aux[2].replace("\n", "")
            schedules[aux2[0]] = aux2[1]

print(schedules)

'''
##  105000001@FUNDAMENTOS FISICOS Y TECNOLOGICOS DE LA INFORMATICA@Basica@6@
'''