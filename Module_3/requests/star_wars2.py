import requests

response = requests.get('https://swapi.dev/api/starships/')
jsonfile = response.json()
for i in jsonfile['results']:
    if i['name'] == 'Millennium Falcon':
        print(i['cost_in_credits'])

