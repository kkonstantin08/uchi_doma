import requests

response = requests.get('https://swapi.dev/api/')
jsonfile = response.json()
response1 = requests.get(jsonfile['people'])
for i in response1.json()["results"]:
    print(i['name'])