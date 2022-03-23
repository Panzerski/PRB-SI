import csv
from random import randint
from decimal import Decimal

limit = 1000
suma = 0
waga = 0
wyniki = []
with open("items_PRB.csv", "r") as file:
    reader = csv.reader(file)
    while True:
        rand = randint(1, 1000)
        next(reader)
        for row in reader:
            if int(row[0]) == rand:
                suma = suma + int(row[2])
                waga += Decimal(row[3])
                if suma >= limit:
                    suma=suma-int(row[2])
                    break
                wyniki.append(row)
                #print(suma)
        if suma + int(row[2]) >= limit:
            break
        file.seek(0)
#print(suma)
#print(waga)
print(wyniki)
