from test_framework import generic_test


def plus_one(A):
    index = len(A) - 1

    while True:
        if A[index] < 9:
            A[index] += 1
            break

        A[index] = 0
        index -= 1

        if index == -1:
            # Must be something like 999 or 99
            # So change first int to 1 and append 0
            A[0] = 1
            A.append(0)
            break

    return A


if __name__ == '__main__':
    print(plus_one([1, 2, 3]))
    print(plus_one([1, 2, 9]))
    print(plus_one([9, 9, 9, 9]))
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
