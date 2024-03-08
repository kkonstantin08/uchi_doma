class Student:
    def __int__(self, name, course):
        self.__name = name
        self.__course = course
        self.__status = 'student'
    def next_course(self):
        if self.course<11:
            self.__course+=1
    def __deduction(self):
        if self.course>11:
            self.__course = 'None'
            self.__status = 'expelled'
    def get_info(self):
        return f''

