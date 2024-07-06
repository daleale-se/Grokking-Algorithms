from .Node import Node 

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
           
    # O(1)
    def add_first(self, item):
        new_node = Node(item)
        if (self.head == None):
            self.head = new_node  
        else: 
            aux_node = self.head
            self.head = new_node
            new_node.next = aux_node
        self.length += 1
        
    # O(n)
    def add_last(self, item):
        if (self.head == None):
            self.head = Node(item)
        else:
            current = self.head
            while not (current.next == None):
                current = current.next
            current.next = Node(item)
        self.length += 1
    
    # O(n)
    def insert(self, item, pos):
        if (0 < pos < self.length):
            if pos == 1:
                self.add_first(item)
            elif pos == self.length:
                self.add_last(item)
            else:
                i = 1
                prev = self.head
                while i < (pos - 1):
                    prev = prev.next
                    i += 1
                new_node = Node(item)
                new_node.next = prev.next
                prev.next = new_node
                self.length += 1
        else:
            print("incorrect position")
    
    def remove_first(self):
        if (not (self.head == None)):
            self.head = self.head.next
            self.length -= 1
        else: 
            print("linkedlist is empty")
        
    def remove_last(self):
        if (not (self.head == None)):
            i = 1
            current = self.head
            while i < (self.length - 1):
                current = current.next
                i += 1
            current.next = None
            self.length -= 1
        else: 
            print("linkedlist is empty")
            
    def remove(self, pos):
        if (0 < pos < self.length):
            if pos == 1:
                self.remove_first()
            elif pos == self.length:
                self.remove_last()
            else:
                i = 1
                prev = self.head
                cur = prev.next
                while i < (pos - 1):
                    prev = cur
                    cur = cur.next
                    i += 1
                prev.next = cur.next
                self.length -= 1
        else:
            print("incorrect position")
    
    def len(self):
        return self.length