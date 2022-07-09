def sort(array):
    index_array = [0 for i in range(len(array))]
    result = []
    starting_row = 0
    while (sum(index_array) != len(array) * len(array[0])):
        lowest_indices = []
        lowest = array[starting_row][index_array[starting_row]]
        for i in range(len(array)):
            if index_array[i] < len(array[0]):
                if array[i][index_array[i]] <= lowest:
                    lowest = array[i][index_array[i]]
                    lowest_indices.append(i)
        result.append(lowest)
        for ind in lowest_indices:
            if array[ind][index_array[ind]] == lowest and index_array[ind] < len(array[0]):
                index_array[ind] += 1
        while not index_array[starting_row] < (len(array[0])):
            if starting_row < len(array):
                starting_row += 1
            if sum(index_array) == len(array) * len(array[0]):
                break
    return result
