from .Node import Node


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    # O(1)
    def enqueue(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    # O(1)
    def dequeue(self):
        if self.length == 0:
            print("the queue is empty")
        else:
            aux_node = self.front
            if aux_node == self.rear:
                self.rear = None
            self.front = aux_node.next
            self.length -= 1
            return aux_node.data

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0
