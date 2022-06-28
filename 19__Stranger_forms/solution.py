from copy import deepcopy



MOVEMENTS = {
    'A': (-1, 0),
    'B': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}



def add_points(p, q):
    px, py = p
    qx, qy = q
    return (px + qx, py + qy)



def outside_of_bounds(point, cinema_layout):
    x, y = point

    MIN_X = 0
    MAX_X = len(cinema_layout) - 1

    MIN_Y = 0
    MAX_Y = len(cinema_layout[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y



def build_layout(configuration, layout):
    layout = deepcopy([list(row) for row in layout])

    for name, point in configuration.items():
        x, y = point
        layout[x][y] = name

        new_layout = []

        for row in layout:
            new_layout.append(''.join(row))

    return new_layout



def in_cinema(point, cinema_layout):
    x, y = point

    return not outside_of_bounds(point, cinema_layout) and cinema_layout[x][y] == '.'



def build_friends_relative_position(friends_configuration):
    relative_position = {}

    for configuration in friends_configuration:
        relative_position[configuration[0]] = (0, 0)

    for configuration in friends_configuration:
        if len(configuration) == 1:
            continue

        name , position, relative_to = configuration

        relative_x, relative_y = relative_position[relative_to]
        dx, dy = MOVEMENTS[position]

        relative_position[name] = (relative_x + dx, relative_y + dy)

    return relative_position



def stranger_forms(cinema_layout, friends_configuration):
    result = []
    friends_relative_position = build_friends_relative_position(friends_configuration)

    for x in range(len(cinema_layout)):
        for y in range(len(cinema_layout[0])):
            if cinema_layout[x][y] == '*':
                continue

            friends_current_posistion = {
                name: add_points((x, y), relative_point)
                for name, relative_point in friends_relative_position.items()
            }

            all_points_in = True

            for point in friends_current_posistion.values():
                if not in_cinema(point, cinema_layout):
                    all_points_in = False
                    break

            if all_points_in:
                result.append(build_layout(friends_current_posistion, cinema_layout))
                

    return result




cinema_layout = ['..*...*.**',
                '.....**...',
                '*.*...*..*',
                '.**....*.*',
                '...*..*.*.',
                '.***...*..',
                '*......*.*',
                '.....**..*',
                '..*.*.*..*',
                '***.*.**..']

friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]

stranger_forms(cinema_layout, friends_configuration)