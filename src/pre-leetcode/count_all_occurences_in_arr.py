def counter(arr):
    counter = {}
    for el in arr:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    return counter

arr = [1, 2, 2, 1, 3, 5]

res = counter(arr)
print(res)