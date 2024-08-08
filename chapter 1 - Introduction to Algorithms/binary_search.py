# O(log n) = logarithmic time
def binary_search(item_list, item):
    low = 0
    high = len(item_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = item_list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None
