from math import factorial

def fact_digits(n):
    n_to_string = str(n)
    string_to_list = [int(char) for char in n_to_string]
    factorials_list = []
    for number in string_to_list:
        get_factorial = factorial(number)
        factorials_list.append(get_factorial)

    return sum(factorials_list)


fact_digits(101)