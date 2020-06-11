from test_framework import generic_test
from heapq import heapify, heappop, heappush, heappushpop
from itertools import islice


def sort_approximately_sorted_array(sequence, k):
    min_heap = []
    index = 0
    for i in islice(sequence, k):
        index += 1
        heappush(min_heap, i)

    result = []
    for next_item in sequence:
        ans = heappushpop(min_heap, next_item)
        result.append(ans)

    for i in range(len(min_heap)):
        result.append(heappop(min_heap))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
