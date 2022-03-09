import csv

with open("items_PRB.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
