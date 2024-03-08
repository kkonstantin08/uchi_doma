class Name:
    def __init__(self,name):
        self.name2=name
    def __repr__(self):
        d=self.__class__.__name__
        return d
a=Name('sksksk')
print(a)