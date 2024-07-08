from classes.LinkedList import LinkedList
from classes.Queue import Queue

# Arrays: Finding the point of insertion/deletion O(1) & Performing the insertion/deletion O(n)
# Linked List: Finding the point of insertion/deletion O(n) & Performing the insertion/deletion O(1)

def print_linked_list(linked_list:LinkedList):
    current = linked_list.head
    while (not (current == None)):
        print(current.item)
        current = current.next
        
def example_linked_list():
    linked_list = LinkedList()
    linked_list.add_last(4)
    linked_list.add_last(9)
    linked_list.add_first(13)
    linked_list.add_first(-1)
    linked_list.insert(-18, 3)
    linked_list.insert(-7, 1)

    print_linked_list(linked_list)
    
    linked_list.remove_last()
    linked_list.remove_first()
    linked_list.remove(9)
    linked_list.remove(2)

    print_linked_list(linked_list)
        
    print("length = ", linked_list.len())

def print_queue(queue: Queue):
    current = queue.front
    while (not (current == None)):
        print(current.item)
        current = current.next
    

def example_queue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(9)
    queue.enqueue(-1)
    queue.enqueue(3)
    
    print_queue(queue)
    print("\n\n")
    
    queue.dequeue()
    queue.dequeue()
    
    print_queue(queue)


def main():
    
    #example_linked_list()
    example_queue()
    
    return 0

main()