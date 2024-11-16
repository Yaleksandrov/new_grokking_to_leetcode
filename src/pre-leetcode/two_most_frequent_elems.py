def two_most_frequent(arr):
    counter = {}
    
    for el in arr:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
     
    first_max, second_max = 0, 0
    fist_max_el, second_max_el = None, None    
    for k, v in counter.items():
        if v > first_max:
            first_max = v
            fist_max_el = k
        elif v < first_max and v > second_max:
            second_max = v
            second_max_el = k
    return fist_max_el, second_max_el

arr = [1, 1, 1, 2, 2, 3, 4, 5,5, 5, 5, 5]

res = two_most_frequent(arr)

print(res)