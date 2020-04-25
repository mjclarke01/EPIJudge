from test_framework import generic_test


def edges(square_matrix):
    result = []

    while square_matrix:
        max_x = len(square_matrix) - 1

        result.extend(square_matrix[0])
        square_matrix.pop(0)

        for y in range(0, len(square_matrix)):
            result.append(square_matrix[y].pop(max_x))

        if square_matrix:
            # Might be empty by the time we get here
            result.extend(reversed(square_matrix[-1]))
            square_matrix.pop(-1)

            for y in range(len(square_matrix)-1, -1, -1):
                result.append(square_matrix[y].pop(0))

    return result


def matrix_in_spiral_order(square_matrix):
    return edges(square_matrix)


if __name__ == '__main__':
    matrix_in_spiral_order([[1]])
    matrix_in_spiral_order([[9, 15, 10, 6], [14, 7, 2, 4], [16, 12, 8, 3], [11, 1, 13, 5]])
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
