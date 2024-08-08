from .Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    # O(1)
    def add_first(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # O(n)
    def add_last(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)
        self.length += 1

    # O(n)
    def insert(self, item, pos):
        if pos < 0 or self.length < pos:
            print("incorrect position")
        elif pos == 0:
            self.add_first(item)
        elif pos == self.length:
            self.add_last(item)
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            new_node = Node(item)
            new_node.next = current.next
            current.next = new_node
            self.length += 1

    # O(1)
    def remove_first(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            self.head = self.head.next
            self.length -= 1

    # O(n)
    def remove_last(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.length -= 1

    # O(n)
    def remove(self, pos):
        if pos < 0 or self.length <= pos:
            print("incorrect position")
        elif pos == 0:
            self.remove_first()
        elif pos == self.length - 1:
            self.remove_last()
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            current.next = current.next.next
            self.length -= 1

    def len(self):
        return self.length
