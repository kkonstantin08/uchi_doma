import json
import csv

# Чтение данных из JSON-файла
with open('files/rate.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создание списка списков с данными
rows = [[valute['CharCode'], valute['Name']] for valute in data['Valute'].values()]

# Сортировка списка по первому элементу каждого подсписка
rows.sort(key=lambda x: x[0])

# Запись данных в CSV-файл
with open('files/currency.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['CharCode', 'Name'])
    writer.writerows(rows)

# Чтение и вывод данных из CSV-файла
with open('files/currency.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    print(*reader.fieldnames)
    for row in reader:
        print(f"{row['CharCode']}, {row['Name']}")
