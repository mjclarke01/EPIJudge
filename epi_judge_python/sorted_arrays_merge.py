from test_framework import generic_test
from heapq import heapify, heappop, heappush


# First attempt - average = 423
def merge_sorted_arrays(sorted_arrays):
    flat_data = []

    for a in sorted_arrays:
        flat_data.extend(a)
    heapify(flat_data)

    result = [heappop(flat_data) for _ in range(len(flat_data))]

    return result


# From the book
def merge_sorted_arrays(sorted_arrays):
    min_heap = []

    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heappush(min_heap, (next_element, smallest_array_i))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
