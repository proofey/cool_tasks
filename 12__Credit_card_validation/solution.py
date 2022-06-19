def sum_digits(reversed_lst):
    result = []
    for i in range(1, len(reversed_lst), 2):
        number = reversed_lst[i] * 2
        
        if number >= 10:
            number = sum([int(char) for char in str(number)])
            result.append(number)
        else:
            result.append(number)
    
    return result

def is_divided_by_10(final_number):
    lst = [int(char) for char in str(final_number)]
    if lst[-1] == 0:
        return True
    else:
        return False


def is_credit_card_valid(number):
    lst = [int(char) for char in str(number)]
    reversed_lst = lst[::-1]
    untouched_digits = [reversed_lst[i] for i in range(0, len(reversed_lst), 2)]
    transformed_digits = sum_digits(reversed_lst)
    final_number = sum(untouched_digits) + sum(transformed_digits)
    result = is_divided_by_10(final_number)
    return result


is_credit_card_valid(79927398713)