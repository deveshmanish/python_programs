def transposeSubArray(array, array_size_x, array_size_y, starting_x, starting_y, sub_array_size):
    if starting_x + sub_array_size <= array_size_x and starting_y + sub_array_size <= array_size_y:
        (i, j) = (starting_x, starting_y)
        while (i < starting_x + sub_array_size and j < starting_y + sub_array_size):
            (x, y, step) = (i, j, 1)
            while (x + step < starting_x + sub_array_size and y + step < starting_y + sub_array_size):
                (array[x + step][y], array[x][y + step]) = (array[x][y + step], array[x + step][y])
                step += 1
            (i, j) = (i + 1, j + 1)
    else:
        print('Incorrect sub-array size or starting point')
