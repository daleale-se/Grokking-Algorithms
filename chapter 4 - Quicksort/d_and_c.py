def min_square_splot(x_pos, y_pos):
    print(x_pos, y_pos)
    if x_pos / 2 == y_pos:
        return y_pos
    elif x_pos > y_pos:
        return min_square_splot(x_pos - y_pos, y_pos)
    else:
        return min_square_splot(y_pos, x_pos)


def array_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + array_sum(arr[1:])


def array_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] > arr[1]:
            arr[1] = arr[0]
        return array_max(arr[1:])
