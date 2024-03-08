import json

with open('files/starwars.json') as file:
    data = json.load(file)

counter = 0
for i in range(len(data['results'])):
    print(data['results'][i]['title'])
    if data['results'][i]['director'] == 'George Lucas':
        counter += 1

print(counter)