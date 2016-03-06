class Node:
    def __init__(self, current=None, next=None):
        self.current = current
        self.next = next

    def __str__(self):
        return str(self.current)


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, item):
        node = Node(item)
        node.next = None
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.length = self.length + 1

    def remove(self):
        self.head.current = self.head