from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    squares = [[] for i in range(9)]
    rows = [[] for i in range(9)]

    # Row
    for i in range(9):
        # Column - easy using filter
        in_col = list(filter(lambda x: x != 0, partial_assignment[i]))
        if len(in_col) != len(set(in_col)):
            return False

        for j in range(9):
            val = partial_assignment[i][j]
            if val:
                # Check the row
                rows[j].append(val)
                if len(rows[j]) != len(set(rows[j])):
                    return False

                # Check the square
                s_num = i // 3 + (j // 3)*3
                if val in squares[s_num]:
                    return False
                else:
                    squares[s_num].append(val)

    return True


if __name__ == '__main__':
    # is_valid_sudoku([[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 8, 0, 9, 0, 0, 5, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 5, 0, 0, 0, 0, 3, 0], [0, 0, 0, 0, 6, 0, 0, 0, 0], [0, 0, 6, 4, 0, 0, 0, 0, 8], [0, 0, 0, 0, 0, 0, 0, 3, 0]])
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
