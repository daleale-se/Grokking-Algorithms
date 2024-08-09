from .Node import Node


class Stack:
    def __init__(self):
        self.front = None
        self.length = 0

    def push(self, data):
        if self.front is None:
            self.front = Node(data)
        else:
            aux_node = self.front
            self.front = Node(data)
            self.front.next = aux_node
        self.length += 1

    def pop(self):
        if self.front is None:
            print("the stack is empty")
        else:
            data = self.front.data
            self.front = self.front.next
            self.length -= 1
            return data
