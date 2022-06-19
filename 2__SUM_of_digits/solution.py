def sum_of_digits(n):
    n_to_string = str(abs(n))
    string_to_list = [int(char) for char in n_to_string]
    return sum(string_to_list)
    

sum_of_digits(123456)