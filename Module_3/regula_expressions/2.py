import re

patern = r'8\(\d{3}\)\d{3}\-\d{2}\-\d{2}'
string = input()
new_string = re.findall(patern, string)
for i in new_string:
    print(i, end=' ')
