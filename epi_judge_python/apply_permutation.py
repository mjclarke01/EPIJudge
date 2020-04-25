from test_framework import generic_test


# Version 1 - swap based on the perm
def apply_permutation(perm, A):
    i = 0
    while i < len(perm):
        if perm[i] == i:
            i += 1
            continue
        j = perm[i]
        perm[i], perm[j] = perm[j], perm[i]
        A[i], A[j] = A[j], A[i]

    return


# Version - basically we are sorting perm and A is "following"
# Would be quicker if we could create a new A, but that would increase the space used.
# def apply_permutation(perm, A):
#     for i, y in enumerate(sorted(zip(perm, A))):
#         A[i] = y[1]
#
#     return


# Textbook - it leaves the permutation as it was at the end, is this important?
# There doesn't appear to be anything in the instructions about it.
# Reading it again, the hint vaguely implies this.
# Without the permutation fix it is slightly quicker than mine.
def apply_permutation(perm, A):
    for i in range(len(A)):
        # Check if the element at index i has not been moved by checking if
        # perm[i] is nonnegative.
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # Subtracts len(perm) from an entry in perm to make it negative,
            # which indicates the corresponding move has been performed.
            perm[next] -= len(perm)
            next = temp
    # Restore perm.
    perm[:] = [a + len(perm) for a in perm]


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    print(apply_permutation_wrapper([2, 0, 1, 3], ['a', 'b', 'c', 'd']))  # b c a d
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
