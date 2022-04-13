import csv
from random import randint

limit = 1000
suma = 0
waga = 0
wyniki = []
with open("items_PRB.csv", "r") as file:
    reader = csv.reader(file)
    while True:
        next(reader)
        rand = randint(1, 1000)
        for row in reader:
            if int(row[0]) == rand:
                if int(row[2]) > limit - suma: break
                suma += int(row[2])
                waga += float(row[3])
                wyniki.append(row)
                #print(suma)
        if suma >= limit: break
        file.seek(0)
print("%.1f" % waga)
print(suma)
print(wyniki)