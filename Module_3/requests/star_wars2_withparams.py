import requests

params = {'search': 'Millennium Falcon'}
response = requests.get('https://swapi.dev/api/starships/', params=params).json()
print(requests.get('https://swapi.dev/api/starships/', params=params).url)
print(response['results'][0]['cost_in_credits'])