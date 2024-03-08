import datetime

string1 = list(map(int, (input().split('.'))))
time_now = datetime.datetime(string1[-1], string1[-2], string1[-3])
string2 = list(map(int, (input().split('.'))))
time_of_birthday = datetime.datetime(string2[-1], string2[-2], string2[-3])
if time_of_birthday.month >= time_now.month:
    birthday_now = datetime.datetime(time_now.year, time_of_birthday.month, time_of_birthday.day)
    delta = birthday_now - time_now
    print(delta.days)
else:
    birthday_now = datetime.datetime(time_now.year+1, time_of_birthday.month, time_of_birthday.day)
    delta = birthday_now - time_now
    print(delta.days)