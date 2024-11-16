arr = [1,2,3,4,5]

arr2 = [1,2,3,4,5,6]

arr3 = [1]

def print_every_second(arr):
    print('Print using For Loop')
    for i in range(1, len(arr), 2):
        print(arr[i], end = ' ')
        
    print('\nPrint using While Loop')
    
    start = 1
    end = len(arr)
    
    while start < end:
        print(arr[start], end = ' ')
        start += 2
    
    print('\n')
        
        
if __name__ == '__main__':
    print_every_second(arr)
    print_every_second(arr2)
    print_every_second(arr3)