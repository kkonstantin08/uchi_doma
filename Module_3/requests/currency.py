import requests

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
print(len(response['Valute']))