from test_framework import generic_test
import heapq


def sort_k_increasing_decreasing_array(A):
    increasing = True
    troughs = []
    start = 0

    for i in range(0, len(A) - 1):
        if A[i] < A[i+1]:
            if not increasing:
                # troughs.append((i - len(A), start - len(A) - 1))
                troughs.append(A[i - len(A): start - len(A) - 1:-1])
                increasing = True
                start = i + 1
        else:
            if increasing:
                # peaks.append((start, i + 1))
                troughs.append(A[start:i+1])
                increasing = False
                start = i + 1
    # troughs.append((-1, start - len(A) - 1))
    if increasing:
        troughs.append(A[start:len(A)])
    else:
        troughs.append(A[-1: start - len(A) - 1:-1])

    return list(heapq.merge(*troughs))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
