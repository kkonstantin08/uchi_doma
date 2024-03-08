file = open(file='documents/lines.txt', mode='r', encoding='utf-8')
counter = 0
for line in file:
    line = line.replace(" ", "")
    if line.isalpha():
        if line == line[::-1]:
            counter += 1

file.close()

print(counter)
