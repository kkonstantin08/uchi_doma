import re

patern = r'(?:[А-Яа-яЁё]+\s){2}[А-Яа-яЁё]+'


string = 'Куташов Константин Александрович'
new_string = re.sub(patern, r'Неизвестный', string)
print(new_string)