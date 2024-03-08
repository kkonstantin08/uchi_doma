class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


n4 = Node('apple', None)
n3 = Node('banana', n4)
n2 = Node('orange', n3)
n1 = Node('grapes', n2)


value = input("Что ищем: ")
position = 1
current_node = n1

while current_node is not None:
    if current_node.value == value:
        break
    current_node = current_node.next
    position += 1

if current_node is None:
    print(-1)
else:
    print(position)