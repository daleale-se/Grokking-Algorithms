def merge(left, right):
    arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    while i < len(left):
        arr.append(left[i])
        i += 1

    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr


def mergesort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)
