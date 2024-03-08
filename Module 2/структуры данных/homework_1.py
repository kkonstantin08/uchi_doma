class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def print_linked_list(vertex):
    while vertex:
        print(vertex.value, end=" -> ")
        vertex = vertex.next
    print("None")


n3 = Node('third', None)
n2 = Node('second', n3)
n1 = Node('first', n2)
head = n1
x = int(input())
position = 0
current_node = n1
if x == 0:
    head = current_node.next
else:
    x1 = n1
    for i in range(x):
        x1 = x1.next
    if x1.next is None:
        val = None
        a1 = n1
        for i in range(x):
            if i == x - 1:
                a1.next = val
            a1 = a1.next
    else:
        while current_node is not None:
            if x == position:
                a = current_node.next
                for i in range(x):
                    a1 = n1
                    if i == x - 1:
                        a1.next = a
                    a1 = a1.next
            current_node = current_node.next
            position += 1

print_linked_list(head)

