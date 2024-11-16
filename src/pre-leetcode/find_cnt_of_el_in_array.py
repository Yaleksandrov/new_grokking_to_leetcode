def find_cnt_in_array(arr, val):
    cnt = 0
    
    for el in arr:
        if el == val:
            cnt += 1
    
    return cnt

arr = [1, 2, 3, -1, 1, 1]

res = find_cnt_in_array(arr, 1)

print(res)