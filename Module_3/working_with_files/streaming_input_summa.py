from sys import stdin

summa = 0
lines = []
for line in stdin:
    lines.append(line.strip('/n').split())

for i in range(len(lines)):
    for j in  range (len(lines[i])):
        summa = summa + int(lines[i][j])

print(summa)