arr = [1,2,3,4,5]

def find_el_in_array(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

if __name__ == '__main__':
    print(f"Positive test {find_el_in_array(arr, 3)}")
    print(f"Negative test {find_el_in_array(arr, 30)}")