arr = [1,2,3,4,5]

def find_idx_target(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            print(f"Target value index is {i}")
            break
    
find_idx_target(arr, 3)