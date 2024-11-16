def sum_in_range(arr, start_idx, end_indx):
    sm = 0
    while start_idx <= end_indx:
        sm += arr[start_idx]
        start_idx += 1
    return sm


tst = [1, 2, 3, 4, 5]
res1 = sum_in_range(tst, 0, 4)
res2 = sum_in_range(tst, 1, 2)

print(res1, res2)