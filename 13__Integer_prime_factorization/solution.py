def sort_primes(n):
    lst_of_n = [i for i in range(2, n + 1)]
    primes = lst_of_n[:]
    for digit in lst_of_n:
        for d in range(2, digit):
            if digit % d == 0:
                primes.remove(digit)
                break
    return primes

def is_prime(n):
    for d in range(2, n):
        if n % d == 0:
            return False
        else:
            return True


def check_for_match(a, b, n):
    result = []
    t1 = [(a ** i, a,  i) for i in range(1, 10)]
    t2 = [(b ** i, b,  i) for i in range(1, 10)]
    for aa in t1:
        for bb in t2:
            if aa[0] * bb[0] == n:
                result.append(aa[1:])
                result.append(bb[1:])
    return result



def prime_factorization(n):
    result = []
    if is_prime(n):
        result.append((n, 1))
    primes = sort_primes(n)
    for a in primes:
        for b in primes:
            matches = check_for_match(a, b, n)
            if matches != []:
                result += matches
    
    return sorted(set(result))

prime_factorization(356)
    
