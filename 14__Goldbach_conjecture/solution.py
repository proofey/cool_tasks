def sort_primes(n):
    lst_of_n = [i for i in range(2, n + 1)]
    primes = lst_of_n[:]
    for digit in lst_of_n:
        for d in range(2, digit):
            if digit % d == 0:
                primes.remove(digit)
                break
    return primes


def goldbach(n):
    result = []
    if n % 2 == 1:
        return None
    primes_of_n = sort_primes(n)
    for a in primes_of_n:
        for b in primes_of_n:
            if a + b == n:
                combination = a, b
                st = tuple(sorted(combination))
                if st not in result:
                    result.append(st)
    return sorted(result)  
    
print(goldbach(4))

