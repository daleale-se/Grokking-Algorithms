from classes.LinkedList import LinkedList

def print_linked_list(linked_list:LinkedList):
    current = linked_list.head
    while (not (current == None)):
        print(current.item)
        current = current.next

def main():
    
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
    
    return 0

main()