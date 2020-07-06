from test_framework import generic_test, test_utils
import heapq


# Naive - use a min-heap => BigO(len(A)) heap operations
def k_largest_in_binary_heap(A, k):
    if k == 0:
        return []

    heap = []

    for item in A:
        if len(heap) < k:
            heapq.heappush(heap, item)
        else:
            heapq.heappushpop(heap, item)
    return heap


# From the book => BigO(k) heap operations
def k_largest_in_binary_heap(A, k):
    if k == 0:
        return []

    max_heap = [(-A[0], 0)]

    result = []
    for _ in range(k):
        index = max_heap[0][1]
        result.append(-heapq.heappop(max_heap)[0])

        left_index = 2 * index + 1
        if left_index < len(A):
            heapq.heappush(max_heap, (-A[left_index], left_index))

        right_index = 2 * index + 2
        if right_index < len(A):
            heapq.heappush(max_heap, (-A[right_index], right_index))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
