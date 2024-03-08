import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto').json()
print(response)
for i in range(response['abilities']):
    if response['abilities']['ability']['name'] == 'pikachu':
        k = 1
        a = response['abilities']['ability']['url']