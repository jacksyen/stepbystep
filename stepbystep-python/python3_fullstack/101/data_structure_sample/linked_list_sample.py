class Node:
    def __init__(self, current=None, next=None):
        self.current = current
        self.next = next

    def __str__(self):
        return str(self.current)


node = Node('test')
node_1 = Node('test1')
print(node)
node.next = node_1
node_1.next = Node("test2")
node_1.next.next = Node("test3")

current=node
while current.next is not None:
    print(current.next)
    current=current.next