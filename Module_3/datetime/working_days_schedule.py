import datetime


string = list(map(int, (input().split('.'))))
date = datetime.datetime(string[-1], string[-2], string[-3])
month = date.month
print(month)
a = 1
while date.month == month:
    if a in [1, 2]:
        print(date.strftime('%d.%m.%Y'), 'рабочий')
        a += 1
        date += datetime.timedelta(days=1)
    elif a in [3, 4]:
        print(date.strftime('%d.%m.%Y'), 'выходной')
        a += 1
        date += datetime.timedelta(days=1)
    else:
        a = 1

