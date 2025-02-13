def binary_search_iterative(array, value):
    array1_end = (len(array) - 1) // 2
    array2_start = (len(array) - 1) // 2

    return_value = None
    if array[array2_start] > value:
        index = 0
        while index < array2_start:
            if array[index] == value:
                return_value = index
            index+=1
    else:
        index = array2_start
        while index < len(array):
            if array[index] == value:
                return_value = index
            index+=1
    return return_value
array = [1, 2, 3]
print(binary_search_iterative(array, 2))