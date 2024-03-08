d = 0
class Point:
    def __init__(self ,x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, a):
        global d
        if a>= 0:
            self.__x = a
        else:
            if d == 0:
                print('Координата должна быть >= 0')
                d +=1

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, s):
        global d
        if s >= 0:
            self.__y = s
        else:
            if d == 0:
                print('Координата должна быть >= 0')
                d +=1

    def __str__(self):
        return f'Point({self.__x}, {self.__y})'


x, y = map(int, input().split())
point = Point()
point.x = x
point.y = y
print(point)