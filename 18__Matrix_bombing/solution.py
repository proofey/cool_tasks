from copy import deepcopy



def sum_matrix(matrix):
    return sum(sum(row) for row in matrix)



def outside_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1

    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y



def bomb_matrix(point, matrix):
    moves = [
        (0, 1),
        (1, 0),

        (1, 1),
        (-1, -1),

        (-1, 1),
        (1, -1),

        (-1, 0),
        (0, -1)
    ]

    point_x, point_y = point
    bomb_value = matrix[point_x][point_y]

    points = [(point_x + move[0], point_y + move[1]) for move in moves]

    for x, y in points:
        if outside_of_bounds((x, y), matrix):
            continue

        current_value = matrix[x][y]
        new_value = current_value - bomb_value
        matrix[x][y] = max(0, new_value)

    return sum_matrix(matrix)



def matrix_bombing_plan(matrix):
    result = {}

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            point = (x, y)
            result[point] = bomb_matrix(point, deepcopy(matrix))

    return result




matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_bombing_plan(matrix)