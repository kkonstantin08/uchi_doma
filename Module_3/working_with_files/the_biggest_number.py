file = open(file='documents/numbers.txt', mode='r', encoding='utf-8')
maxx = 0
for line in file:
    s = []
    a = line.strip('/n')
    print(a)
    s = list(map(int, a.split()))
    print(s)
    if max(s) > maxx:
        maxx = max(s)
print(maxx)


