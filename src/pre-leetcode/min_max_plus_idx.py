def min_max(arr):
    min = float('inf')
    max = -float('inf')
    min_idx, max_idx = 0, 0 
    
    for i in range(len(arr)):
        if arr[i] < min:
            min  = arr[i]
            min_idx = i
        elif arr[i] > max:
            max = arr[i]
            max_idx = i
            
    return {
        'min': [min, min_idx],
        'max': [max, max_idx]
    }

arr = [1, 2, 3, 4]
res = min_max(arr)

print (f"Minimum element if array {arr} is {res['min'][0]} with index {res['min'][1]}, max element is {res['max'][0]} with index {res['max'][1]}")

arr = [-1, 2, -3, 4]
res = min_max(arr)

print (f"Minimum element if array {arr} is {res['min'][0]} with index {res['min'][1]}, max element is {res['max'][0]} with index {res['max'][1]}")