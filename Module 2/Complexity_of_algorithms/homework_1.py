x = list(map(int, input().split()))
total = int(input())
b = []
for i in x:
    a = i
    for m in x[a:]:
        if a+m == total:
            b.append(a)
            b.append(m)
if len(b) == 0:
    print('None')
else:
    print(b[0], b[1])
