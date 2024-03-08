def proverka_1(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        raise ValueError
    if c == 0:
        raise ZeroDivisionError



try:
    x1, x2, friends = map(int,input().split())
    proverka_1(x1, x2, friends)
except ValueError as e:
    print(e.__class__.__name__)
except ZeroDivisionError as e:
    print(e.__class__.__name__)
else:
    print((x1+x2)//friends)