def array_sum(arr):
    arr_sum = 0
    
    for el in arr:
        arr_sum += el
    
    return arr_sum


print(f"Sum of the array {array_sum([1, 2, 3])}")