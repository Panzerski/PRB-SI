import csv
from random import randint

limit = 1000
HM = []
HMS = 10
suma = [0] * HMS
waga = [0] * HMS
wyniki = []

with open("items_PRB.csv", "r") as file:
    reader = csv.reader(file)
    for i in range(0, HMS):
        wyniki.clear()
        while True:
            next(reader)
            rand = randint(1, 1000)
            for row in reader:
                if int(row[0]) == rand:
                    if int(row[2]) > limit - suma[i]:
                        break
                    suma[i] += int(row[2])
                    waga[i] += float(row[3])
                    wyniki.append(row)
                    # print(suma)
            if suma[i] >= limit:
                break
            file.seek(0)
        file.seek(0)
        HM.append(wyniki)
        print("waga:  %.1f" % waga[i])
        print("cena: ", suma[i])

print(HM)
