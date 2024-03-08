class Person:
    def __init__(self, name, age, passport):
        self.__name = name
        self.__age = age
        self.__passport = passport

    def change_age(self):
        self.__age += 1

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, x):
        if len(str(x)) == 10:
            self.__passport = x
        else:
            print('Неверный номер паспорта')

    def get_info(self):
        a= '*'*6 + str(self.__passport)[-1:-5:-1]
        return f'{self.__name}, возраст: {self.__age}, номер паспорта: {a}'


name = input()
age = int(input())
passport = int(input())
method = input()
person = Person(name, age, passport)
if method == 'change_age':
    person.change_age()
else:
    person.passport = int(method)
print(person.get_info())