"""
[1, 2, 3, 4]
[1, 1* 2, 1*2*3, 1*2*3*4]
[1, 2, 6, 24]
prev = 1
curr = curr*prev
prev = curr, curr= curr.next

"""

def prefix_sum(arr):
    prev = 1
    
    for i in range(len(arr)):
        arr[i] = arr[i]* prev
        prev = arr[i]
        
    return arr

arr = [1,2, 3,4]
res = prefix_sum(arr)

print(res)
