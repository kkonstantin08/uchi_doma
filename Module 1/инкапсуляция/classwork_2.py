class Point:
    __slots__ = ('__x','__y')
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value >= 0:
            self.__x = value
        else:
            print('Координата должна быть > 0')


    def get_y(self):
        return self.__y


    def set_y(self, value):
        if value >= 0:
            self.__y = value
        else:
            print('Координата должна быть > 0')

    def __str__(self):
        return f'Point({self.__x}, {self.__y})'


p = Point()
p.x = 10
p.set_y(10)
p.z = 111       #__slots__ = ('__x','__y')


print(p, p.z)
