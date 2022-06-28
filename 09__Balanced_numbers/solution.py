def is_number_balanced(number):
    lst = [int(char) for char in str(number)]
    if len(lst) == 1:
        return True
    
    left_side = lst[0:len(lst) // 2]
    
    if len(lst) % 2 == 0:
        right_side = lst[len(lst) // 2:]
    else:
        right_side = lst[len(lst) // 2 + 1:]

    if sum(left_side) == sum(right_side):
        return True
    else:
        return False
    
is_number_balanced(45245)