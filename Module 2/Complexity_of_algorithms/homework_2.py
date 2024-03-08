maxx = 0
size = 0


class StackMax:
    def __init__(self):
        self.stack = []

    def push(self, item):
        global maxx, size
        self.stack.append(item)
        size += 1
        if size == 2:
            if self.stack[0] > self.stack[1]:
                maxx = self.stack[0]
            elif self.stack[0] == self.stack[1]:
                maxx = self.stack[0]
            else:
                maxx = self.stack[1]
        if size > 2:
            if item > maxx:
                maxx = item

    def pop(self):
        global size
        if size == 0:
            print('error')
        else:
            print(self.stack.pop())
            size -= 1

    @staticmethod
    def size():
        global size
        print(size)

    @staticmethod
    def get_max():
        global maxx
        print(maxx)


test = StackMax()
n = int(input())
list_of_commands = []
for i in range(n):
    a = list(input().split())
    list_of_commands.append(a)
print(list_of_commands)
for i in range(n):
    if list_of_commands[i][0] == 'push':
        test.push(int(list_of_commands[i][1]))
    if list_of_commands[i][0] == 'get_max':
        test.get_max()
    if list_of_commands[i][0] == 'size':
        test.size()
    else:
        test.pop()
