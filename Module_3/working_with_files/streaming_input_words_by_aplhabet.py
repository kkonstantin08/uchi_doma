from sys import stdin

letters = {}
lines = []
for line in stdin:
    lines.append(line.strip('/n').split())

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j][0] not in letters.values():
            letters.update({lines[i][j][0]: []})

for i in letters.keys():
    for j in range(len(lines)):
        for m in range(len(lines[j])):
            if i == lines[j][m][0]:
                letters[i].append(lines[j][m])  # добавляем значение в список

sorted_letters = dict(sorted(letters.items()))
for key in sorted_letters.keys():
    sorted_letters[key].sort()

for key, value in sorted_letters.items():
    a = (' '.join(value))
    print("{} : {}".format(key, a))
