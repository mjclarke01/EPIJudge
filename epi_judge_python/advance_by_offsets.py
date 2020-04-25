from test_framework import generic_test

dead_ends = set()


# def recu(A, i):
#     if i in dead_ends:
#         return False
#
#     if i > len(A):
#         return False
#
#     if i == len(A) or A[i] + i == len(A) - 1:
#         return True
#     if A[i] == 0:
#         return False
#
#     for j in reversed(range(1, A[i] + 1)):
#         ans = recu(A, i + j)
#         if ans:
#             return True
#     if i not in dead_ends:
#         dead_ends.add(i)
#     return False
#
#
# def can_reach_end(A):
#     dead_ends.clear()
#     # If one element then that is a True
#     if len(A) == 1:
#         return True
#     # If there are no zeroes then it is a True
#     if 0 not in A:
#         return True
#
#     return recu(A, 0)


# Much quicker than the recursive version
# ~20,000 faster in one case
# def can_reach_end(A):
#     # If one element then that is a True
#     if len(A) == 1:
#         return True
#     # If there are no zeroes then it is a True
#     if 0 not in A:
#         return True
#
#     # Find the zeroes and see if we can get across it
#     for i in range(len(A)):
#         if A[i] == 0:
#             found = False
#             # Step back to see if we can clear it
#             for j in reversed(range(i)):
#                 # Check for an early win
#                 if j + A[j] >= len(A) - 1:
#                     return True
#
#                 # Can we jump it?
#                 if j + A[j] > i:
#                     found = True
#                     break
#             if not found:
#                 return False
#
#     return True


# Textbook
# With my enhancements it is quicker:
# * return True if only one element
# * return True if no zeroes present
# * check for early win
# * replace call to 'max' with a simple comparison
def can_reach_end(A):
    # If one element then that is a True
    if len(A) == 1:
        return True
    # If there are no zeroes then it is a True
    if 0 not in A:
        return True

    furthest_reach_so_far = 0
    last_index = len(A) - 1
    i = 0
    while i <= furthest_reach_so_far < last_index:
        if A[i] + i > furthest_reach_so_far:
            furthest_reach_so_far = A[i] + i
        # furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
        # Check for early win
        if furthest_reach_so_far > last_index or \
                furthest_reach_so_far + A[furthest_reach_so_far] >= last_index:
            return True
    return furthest_reach_so_far >= last_index


if __name__ == '__main__':
    # print(True is can_reach_end([0]))                             # T
    # print(True is can_reach_end([3]))                             # T
    # print(True is can_reach_end([3, 0, 0]))                       # T
    # print(True is can_reach_end([3, 0, 0, 0]))                     # T
    # print(False is can_reach_end([3, 0, 0, 0, 0]))                 # F
    # print(True is can_reach_end([3, 0, 0, 1]))                    # T
    # print(True is can_reach_end([3, 3, 1, 0, 2, 0, 1]))           # T
    # print(False is can_reach_end([3, 2, 0, 0, 2, 0, 1]))           # F
    # print(True is can_reach_end([5, 1, 4, 0, 1, 0, 0]))           # T
    # print(True is can_reach_end([6, 1, 2, 3, 6, 7, 2, 0, 2, 10, 0, 9, 2, 6]))  # T
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
