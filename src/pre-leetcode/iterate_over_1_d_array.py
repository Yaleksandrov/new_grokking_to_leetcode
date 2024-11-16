arr = [1, 2, 3, 4, 5]

def print_elements(arr):
    print("\nRef: Print elements uning foreach loop")
    for el in arr:
        print(el, end=' ')
    
    print("\nRef: Print elements uning for loop")

    for i in range(len(arr)):
        print(arr[i], end=' ')

    print("\nRef: Print elements uning while loop")

    start, end = 0, len(arr)
    while start < end:
        print(arr[start], end=' ')
        start += 1

if __name__ == '__main__':
    print_elements(arr)
    print('\n')