arr = [100, 26, 13, 6, 7, 3, 1, 0]

def print_primes(arr):
    primes = []

    arr.sort()
    
    for el_to_check in arr:
        if el_to_check < 2:
            primes.append(el_to_check)
        else:
            is_prime = True
            for divider in range(2, el_to_check):
                if el_to_check % divider == 0:
                    is_prime = False
            if is_prime:
                primes.append(el_to_check)
    
    return primes

if __name__ == '__main__':
    res = print_primes(arr)
    print(res)