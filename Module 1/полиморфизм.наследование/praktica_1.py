class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'Человек: {self.name}'

    def det_age(self):
        return f'Возраст: {self.age}'


class Student (Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def get_name(self):
        return f'Ученик: {self.name}({self.course} класс)'
x1=input()
x2=int(input())
x3=int(input())
a=Student(x1, x2, x3)
print(a.get_name())
print(a.det_age())