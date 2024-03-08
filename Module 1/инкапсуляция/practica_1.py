class Student:
    def __init__(self, name, course):
        self.__name = name
        self.__course = course
        self.__status = 'student'

    def next_course(self):
        self.__course += 1
        if self.__course>=11:
            self.__course = 'None'
            self.__status = 'graduate'

    def deduction(self):
        self.__course = 'None'
        self.__status = 'expelled'

    def get_info(self):
        return f'Student: {self.__name} ({self.__course}), status: {self.__status}'


x2 = input()
x3 = int(input())
x1 = input()
student = Student(x2, x3)
if x1 == 'next_course':
    student.next_course()
else:
    student.deduction()
print(student.get_info())