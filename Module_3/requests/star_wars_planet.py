import requests

response = requests.get('https://swapi.dev/api/films/').json()
a = 0
x = 0
for i in response['results']:
    if i['title'] == ' Attack of the Clones':
        x = response['results'][i]['planets']
        break
print(x)
