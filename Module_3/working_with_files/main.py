file = open(file='numbers.txt', mode='r', encoding='utf-8')
lines = []
summa = 0
for line in file:
    a = line.strip('/n')
    lines.append(a.split())
file.close()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        summa = summa + int(lines[i][j])
print(summa)
