import csv

name = ''
height = 0
with open('files/starwars.csv', newline='') as file:
    data = csv.DictReader(file)
    for line in data:
        if line['height'] != 'NA':
            if int(line['height']) > height:
                height = line['height']
                name = line['name']

print(name)
#
# import csv
#
# with open('files/starwars.csv', newline='') as file:
#     data = csv.DictReader(file)
#     characters = {}
#     for line in data:
#         characters[line['name']] = int(line['height']) if line[
#                                                               'height'] != 'NA' else -1
#
# max_height = max(characters.values())
# print(max_height)
# for name, height in characters.items():
#     if height == max_height:
#         print(name)
