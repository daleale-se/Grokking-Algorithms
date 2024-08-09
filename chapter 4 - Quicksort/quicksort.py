import random


# worst case scenario O(n ** 2)
# average case scenario O(n Log n)

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        less, equal, greater = [], [], []
        pivot = arr[random.randint(0, len(arr) - 1)]
        for i in range(len(arr)):
            if arr[i] > pivot:
                greater.append(arr[i])
            elif arr[i] == pivot:
                equal.append(arr[i])
            else:
                less.append(arr[i])
        return quicksort(less) + equal + quicksort(greater)
