import csv

counter = 0
with open(file='files/ratings.csv', encoding='utf-8') as file:
    data = csv.DictReader(file)
    for line in data:
        if line['Genres'] == 'drama':
            counter += 1

print(counter)
