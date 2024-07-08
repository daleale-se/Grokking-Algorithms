from .Node import Node

class Queue():
    
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        self.length += 1
        
    def dequeue(self):
        aux_node = self.front
        self.front = aux_node.next
        return aux_node
    
