def palindromes_count(n):
    counter = 0
    for number in range(10, n + 1):
        if str(number) == str(number)[::-1]:
            counter += 1

    return counter

palindromes_count(20)