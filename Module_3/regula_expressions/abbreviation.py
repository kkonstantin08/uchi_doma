import re

string = input()
pattern = r'[А-Я][А-Я]+'
new_string = re.findall(pattern, string)
for i in new_string:
    print(i, end=' ')