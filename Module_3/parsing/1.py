import requests
from bs4 import BeautifulSoup

url = "https://peps.python.org/#numerical-index"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все элементы с тегом 'li'
li_elements = soup.find_all('td')

count = 0
for li in li_elements:
    # Если 'Warsaw' есть в тексте элемента, увеличиваем счетчик
    if 'Warsaw' in li.text:
        count += 1

print(f"Количество PEP, в авторах которых указан 'Warsaw': {count}")
