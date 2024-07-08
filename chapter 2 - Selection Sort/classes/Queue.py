from .Node import Node

class Queue():
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1
        
    def dequeue(self):
        aux_node = self.front
        self.front = aux_node.next
        return aux_node
    
