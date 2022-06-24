TO_NUMBERS = {
    'a': [2],
    'b': [2, 2],
    'c': [2, 2, 2],
    'd': [3],
    'e': [3, 3],
    'f': [3, 3, 3],
    'g': [4],
    'h': [4, 4],
    'i': [4, 4, 4],
    'j': [5],
    'k': [5, 5],
    'l': [5, 5, 5],
    'm': [6],
    'n': [6, 6],
    'o': [6, 6, 6],
    'p': [7],
    'q': [7, 7],
    'r': [7, 7, 7],
    's': [7, 7, 7, 7],
    't': [8],
    'u': [8, 8],
    'v': [8, 8, 8],
    'w': [9],
    'x': [9, 9],
    'y': [9, 9, 9],
    'z': [9, 9, 9, 9],
    ' ': [0]
}

def message_to_numbers(message):
    result = []
    for i, char in enumerate(message):

        if char.isupper():
            result.append(1)

        key = char.lower()
        numbers = TO_NUMBERS[key]

        if i > 0 and numbers[0] == TO_NUMBERS[message[i - 1].lower()][0]:
            result.append(-1)

        result.extend(numbers)

    return result


message_to_numbers("abc")
[2, -1, 2, 2, -1, 2, 2, 2]