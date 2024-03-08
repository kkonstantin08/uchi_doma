
class Name:
    def __init__(self,name):
        self.name2=name
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name2})'
class Student(Name):
    def get_action(self):
        return f'Ученик{self.name2} учится'
class Teacher(Name):
    def get_action(self):
        return f'Учитель{self.name2} учит'
n=int(input())
x1=[]
x2=[]
actions = {'Student': Student,
               'Teacher': Teacher}
for i in range(n):
    x=input().split(':')
    x1.extend(x)
for i in range(0,len(x1)-1,2):
    s=actions[x1[i]](x1[i+1])
    s1=s.__repr__()
    x2.append(s1.replace(' ','',1))
print(x2)
for i in range(0,len(x1)-1,2):
    s=actions[x1[i]](x1[i+1])
    print(s.get_action())