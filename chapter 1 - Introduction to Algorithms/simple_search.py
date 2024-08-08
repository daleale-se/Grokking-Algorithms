# O(n) = linear time
def simple_search(item_list, item):
    i = 0
    while i < len(item_list):
        if item_list[i] == item:
            return i
        i += 1   
    return None
