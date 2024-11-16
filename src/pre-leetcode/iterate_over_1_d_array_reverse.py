arr = [1,2,3,4,5]

def print_reverse(arr):
    
    print("Print using Python build in function")
    
    print(arr[::-1])
    
    print('\nPrint using reversed range')
    
    for i in reversed(range(len(arr))):
        print(arr[i], end=' ')
        
    print('\nPrint using ForEach loop')
    
    for el in arr[::-1]:
        print(el, end=' ')
    
    print('\n Print using while loop')
    
    start = len(arr) - 1
    end = 0 
    
    while start >= end:
        print(arr[start], end=' ')
        start -= 1
        
    print('\n')
    
if __name__ == '__main__':
    print_reverse(arr)