def sum_matrix(m):
    result = []
    for row in m:
        for col in row:
            result.append(col)

    return sum(result)

sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
