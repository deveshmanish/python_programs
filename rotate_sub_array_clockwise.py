import transpose_sub_array


def rotateSubArray(array, array_size_x, array_size_y, starting_x, starting_y, sub_array_size):
    transpose_sub_array.transposeSubArray(array, array_size_x, array_size_y, starting_x, starting_y, sub_array_size)
    (i, j) = (starting_x, starting_y)
    while (i < starting_y + sub_array_size):
        step = 0
        while (step < sub_array_size - 1):
            (array[i][j + step], array[i][j + sub_array_size - 1 - step]) = (
                array[i][j + sub_array_size - 1 - step], array[i][j + step])
            step += 1
        i += 1
