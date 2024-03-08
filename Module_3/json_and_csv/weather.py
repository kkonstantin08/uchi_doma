import json

with open('files/weather.json', encoding='utf-8') as file:
    data = json.load(file)

temp_max = 0
for i in range(len(data['list'])):
    a = data['list'][i]['main']['temp_max']
    if a > temp_max:
        temp_max = a

print(temp_max)