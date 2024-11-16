def min_max(arr):
    min = float('inf')
    max = -float('inf')
    
    for el in arr:
        if el < min:
            min = el
        elif el >= max:
            max = el
    
    return(min, max)


print(f"Mininmum of the array {[1, 2, 3]} is {min_max([1, 2, 3])[0]}, maximum is {min_max([1, 2, 3])[1]}")