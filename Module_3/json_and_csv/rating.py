import csv

maxx = 0
counter = 0
with open(file='files/ratings.csv', encoding='utf-8') as file:
    data = csv.DictReader(file)
    for line in data:
        if float(line['IMDb Rating']) > maxx:
            maxx = float(line['IMDb Rating'])
            counter = 1
        if float(line['IMDb Rating']) == maxx:
            counter += 1

print(counter)