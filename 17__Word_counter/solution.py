from enum import Enum


class Direction(Enum):
    HORIZONTAL_LEFT = "HORIZONTAL_LEFT"
    HORIZONTAL_RIGHT = "HORIZONTAL_RIGHT"

    VERTICAL_DOWN = "VERTICAL_DOWN"
    VERTICAL_UP = "VERTICAL_UP"

    DIAGONAL_UP_RIGHT = "DIAGONAL_UP_RIGHT"
    DIAGONAL_UP_LEFT = "DIAGONAL_UP_LEFT"

    DIAGONAL_DOWN_RIGHT = "DIAGONAL_DOWN_RIGHT"
    DIAGONAL_DOWN_LEFT = "DIAGONAL_DOWN_LEFT"


def outside_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1

    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y


def take_word(n, point, direction, matrix):
    difference_x = 0 
    difference_y = 0

    if direction == Direction.HORIZONTAL_RIGHT:
        difference_x = 0
        difference_y = 1

    if direction == Direction.HORIZONTAL_LEFT:
        difference_x = 0
        difference_y = -1

    if direction == Direction.VERTICAL_DOWN:
        difference_x = 1
        difference_y = 0

    if direction == Direction.VERTICAL_UP:
        difference_x = -1
        difference_y = 0

    if direction == Direction.DIAGONAL_UP_RIGHT:
        difference_x = -1
        difference_y = 1

    if direction == Direction.DIAGONAL_UP_LEFT:
        difference_x = -1
        difference_y = -1

    if direction == Direction.DIAGONAL_DOWN_RIGHT:
        difference_x = 1
        difference_y = 1

    if direction == Direction.DIAGONAL_DOWN_LEFT:
        difference_x = 1
        difference_y = -1


    start_x, start_y = point
    n_counter = 0
    chars = []

    while n_counter != n:
        if outside_of_bounds((start_x, start_y), matrix):
            return None

        chars.append(matrix[start_x][start_y])

        start_x += difference_x
        start_y += difference_y

        n_counter += 1

    return "".join(chars)


def word_counter(matrix, word):
    result = 0

    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[0])):
            for direction in Direction:
                found_word = take_word(
                    len(word),
                    (row_index, col_index),
                    direction,
                    matrix
                )

                if found_word == word:
                    result += 1

    if word == word[::-1]:
        result //= 2

    return result



word = "ana"
matrix = [
    ["i", "a", "n", "a"],
    ["e", "a", "n", "h"],
    ["i", "n", "n", "v"],
    ["m", "v", "a", "a"],
    ["a", "n", "a", "t"]
]
word_counter(matrix, word)
