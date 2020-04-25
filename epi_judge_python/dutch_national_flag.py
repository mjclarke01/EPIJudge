import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition1(pivot_index, A):
    """
    Two loops.

    :param pivot_index:
    :param A:
    :return:
    """
    pivot_val = A[pivot_index]

    # Less than
    i = 0
    j = len(A) - 1

    while i < j:
        if A[i] < pivot_val:
            i += 1
        else:
            if A[j] >= pivot_val:
                j -= 1
            else:
                A[i], A[j] = A[j], A[i]

    # Equal
    j = len(A) - 1
    while i < j:
        if A[i] <= pivot_val:
            i += 1
        else:
            if A[j] != pivot_val:
                j -= 1
            else:
                A[i], A[j] = A[j], A[i]

    return A


def dutch_flag_partition2(pivot_index, A):
    """
    Use more space, but one loop.

    :param pivot_index:
    :param A:
    :return:
    """
    pivot_val = A[pivot_index]
    ans = A[:]

    i = 0
    j = len(A) - 1

    # Stick the ones below at the front and the ones above at the back
    for v in ans:
        if v < pivot_val:
            A[i] = v
            i += 1
        elif v > pivot_val:
            A[j] = v
            j -= 1

    # Fill the middle with the pivot value
    while i <= j:
        A[i] = pivot_val
        A[j] = pivot_val
        i += 1
        j -= 1

    return A


def dutch_flag_partition(pivot_index, A):
    """
    In place using original space.

    :param pivot_index:
    :param A:
    :return:
    """
    pivot_val = A[pivot_index]

    i = 0
    j = 0
    k = len(A) - 1

    while i <= k:
        if A[i] < pivot_val:
            A[i], A[j] = A[j], A[i]
            j += 1
            i += 1
        elif A[i] > pivot_val:
            A[i], A[k] = A[k], A[i]
            k -= 1
            continue
        else:
            i += 1

    return A

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    print("============= 3")
    print(dutch_flag_partition(3, [0, 1, 2, 0, 2, 1, 1]))
    print("============= 1")
    print(dutch_flag_partition(1, [0, 1, 2, 0, 2, 1, 1]))
    print("============= 2")
    print(dutch_flag_partition(2, [0, 1, 2, 0, 2, 1, 1]))

    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
