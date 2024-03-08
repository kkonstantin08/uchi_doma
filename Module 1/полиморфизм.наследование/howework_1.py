class list:
    def get_even(self):
        self.y = [x for x in self.x if x % 2 == 0]
        return  self.y
    def get_odd(self):
        self.b = [x for x in self.x if x % 2 != 0]
        return self.b
class OddevenList(list):
    def __init__(self, lst):
        self.x=lst
n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
print(lst)
a=OddevenList(lst)
print(a.get_odd())
print(a.get_even())