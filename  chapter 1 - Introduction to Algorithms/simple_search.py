# O(n) = linear time
def simple_search(list, item):
    i = 0
    while (i < len(list)):
        if(list[i] == item):
            return i
        i += 1   
    return None