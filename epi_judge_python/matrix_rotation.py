from test_framework import generic_test
import copy


# With a copy
def rotate_matrix(square_matrix):
    # for i in square_matrix:
    #     print(i)

    original = copy.deepcopy(square_matrix)

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    r_dir_i = 0
    r_dir = directions[r_dir_i]
    r_pos = [0, 0]

    w_dir_i = r_dir_i + 1
    w_dir = directions[w_dir_i]
    w_pos = [0, len(square_matrix) - 1]

    for _ in range(len(square_matrix) * len(square_matrix)):
        square_matrix[w_pos[0]][w_pos[1]] = original[r_pos[0]][r_pos[1]]
        original[r_pos[0]][r_pos[1]] = 0
        next_pos = [r_pos[0] + r_dir[0], r_pos[1] + r_dir[1]]
        if (
            next_pos[0] == len(square_matrix)
            or next_pos[0] < 0
            or next_pos[1] == len(square_matrix)
            or next_pos[1] < 0
            or original[next_pos[0]][next_pos[1]] == 0
        ):
            # Change dir
            r_dir_i = (r_dir_i + 1) & 3
            w_dir_i = (r_dir_i + 1) & 3

            r_dir = directions[r_dir_i]
            w_dir = directions[w_dir_i]
            next_pos = [r_pos[0] + r_dir[0], r_pos[1] + r_dir[1]]

        r_pos = next_pos
        w_pos = [w_pos[0] + w_dir[0], w_pos[1] + w_dir[1]]

    # for i in square_matrix:
    #     print(i)


# Without a copy
# Starts with the outer "ring" then steps in to the next-most outer "ring"
# and so on...
# Uses python's inbuilt swap mechanism
# Essentially the same technique as the book but slightly more verbose
def rotate_matrix(square_matrix):
    # for i in square_matrix:
    #     print(i)

    half_way = len(square_matrix) // 2
    count = 0

    while count < half_way:
        tl = [count, count]
        tr = [count, ~count]
        br = [~count, ~count]
        bl = [~count, count]

        for i in range(count, len(square_matrix) - 1 - count):
            # Rotate the selected elements
            (square_matrix[tr[0]][tr[1]], square_matrix[br[0]][br[1]],
             square_matrix[bl[0]][bl[1]],
             square_matrix[tl[0]][tl[1]]) = (square_matrix[tl[0]][tl[1]],
                                             square_matrix[tr[0]][tr[1]],
                                             square_matrix[br[0]][br[1]],
                                             square_matrix[bl[0]][bl[1]],
                                            )
            # Then select the next element
            tl[1] += 1
            tr[0] += 1
            br[1] -= 1
            bl[0] -= 1

        count += 1

    # for i in square_matrix:
    #     print(i)


# Further refactoring brings us close to the book's solution
def rotate_matrix(square_matrix):
    for i in range(len(square_matrix) // 2):
        # tl = [i, i]
        # tr = [i, ~i]
        # br = [~i, ~i]
        # bl = [~i, i]

        for j in range(i, len(square_matrix) - 1 - i):
            # Rotate the selected elements
            (square_matrix[j][~i], square_matrix[~i][~j],
             square_matrix[~j][i],
             square_matrix[i][j]) = (square_matrix[i][j],
                                     square_matrix[j][~i],
                                     square_matrix[~i][~j],
                                     square_matrix[~j][i],
                                    )
            # Then select the next element
            # tl[1] += 1
            # tr[0] += 1
            # br[1] -= 1
            # bl[0] -= 1


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == "__main__":
    # rotate_matrix([[1]])
    # rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    exit(
        generic_test.generic_test_main(
            "matrix_rotation.py", "matrix_rotation.tsv", rotate_matrix_wrapper
        )
    )
