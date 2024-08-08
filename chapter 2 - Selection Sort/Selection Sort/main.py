

def selection_sort(my_list):
    for i in range(len(my_list)):
        minimum_index = i
        for j in range(i, len(my_list)):
            if my_list[j] < my_list[minimum_index]:
                minimum_index = j
        aux_item = my_list[i]
        my_list[i] = my_list[minimum_index]
        my_list[minimum_index] = aux_item
    return my_list


def main():

    my_list = [2, 8, 5, 3, 9, 4, 1]
    print(selection_sort(my_list))


main()