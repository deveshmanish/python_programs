import transpose_sub_array

def rotateSubArray(array,array_size_x,array_size_y,starting_x,starting_y,sub_array_size):
    transpose_sub_array.transposeSubArray(array,array_size_x,array_size_y,starting_x,starting_y,sub_array_size)
    (i,j) = (starting_x,starting_y)
    while(j<starting_x+sub_array_size):
        step = 0
        while(step<sub_array_size-1):
            (array[i+step][j],array[i+sub_array_size-1-step][j]) = (array[i+sub_array_size-1-step][j],array[i+step][j])
            step += 1
        j += 1