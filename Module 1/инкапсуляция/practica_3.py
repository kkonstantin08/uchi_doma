class Checker:
    def __init__(self, coords):
        n=0
        for x in coords:
            if x >= 0:
                n += 1
        if n == len(coords):
            self.__coords = coords
        else:
            print('Неверная позиция')
            self.__coords = (1, 1)

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, s):
        n = 0
        for x in s:
            if x >= 0:
                n += 1
        if n == len(s):
            self.__coords = s
        else:
            print('Неверная позиция')
            self.__coords = (1, 1)


a1 = tuple(map(int, input().split()))
a2 = tuple(map(int, input().split()))
ch = Checker(a1)
ch.coords = a2
print(ch.coords)