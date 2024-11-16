def find_two_min_max(arr):
    first_min, second_min = float('inf'), float('inf')
    first_max, second_max = -float('inf'), -float('inf')
    
    for el in arr:
        if el < first_min:
            first_min = el
        elif el > first_min and el < second_min:
            second_min = el
        elif el > first_max:
            first_max = el
        elif el < first_max and el > second_max:
            second_max = el
    
    return {
        'min': (first_min, second_min),
        'max': (first_max, second_max)
    }
    
import random

def genertate_arr(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-100, 100))
    return arr

tst = genertate_arr(10)
print(tst, min(tst), max(tst))
res = find_two_min_max(tst)
print(res)
