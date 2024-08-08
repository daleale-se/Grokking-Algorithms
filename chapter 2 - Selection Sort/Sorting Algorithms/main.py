def selection_sort(arr):
    for i in range(len(arr)):
        k = i
        for j in range(i, len(arr)):
            if arr[j] < arr[k]:
                k = j
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            temp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = temp
            j -= 1


def main():

    my_list = [2, 8, 5, 3, 9, 4, 1]
    # selection_sort(my_list)
    # bubble_sort(my_list)
    insertion_sort(my_list)
    print(my_list)


main()