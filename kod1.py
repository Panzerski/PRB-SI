import csv
from random import randint

limit = 1000
#rand = randint(1, 1001)
suma = 0
wyniki = []
with open("items_PRB.csv", "r") as file:
    reader = csv.reader(file)
    while suma <= limit:
        rand = randint(1, 1001)
        for row in reader:
            if int(row[0]) == rand and int(row[2]) <= 1000:
                print(row)
                suma += int(row[2])
                wyniki.append(row)

print(wyniki)