from itertools import groupby

KEYPAD = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
    0: ' '
}

def get_index(key, item):
    index = 0
    for i in range(len(item)):
        if i >= len(KEYPAD[key]):
            index = 0
        index += 1
    return index - 1

def numbers_to_message(pressed_sequence):
    result = ''
    lower = True
    grouped_seq = [list(iterator) for i,iterator in groupby(pressed_sequence)]
    
    for item in grouped_seq:
        key = item[0]

        if key == -1:
            continue
        
        if key == 1:
            lower = False
            continue
        
        index = get_index(key, item)
        letter = KEYPAD[key][index]
        
        if not lower:
            result += letter.upper()
            lower = True
        else:    
            result += letter

    return result


numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
"abc"