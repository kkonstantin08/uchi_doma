class Queue :
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append((item))

    def pop(self):
        print(self.queue.pop(0))

    def sixe(self):
        print(len(self.queue))


a = Queue()
n = int(input())
listt = []
for i in range(n):
    x=list(input().split())
    listt.append(x)
for i in range(len(listt)):
    if listt[i][0] == 'push':
        a.push(int(listt[i][1]))
    if listt[i][0] == 'pop':
        a.pop()
    if listt[i][0] == 'size':
        a.sixe()