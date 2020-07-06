from test_framework import generic_test
import heapq


def online_median(sequence):
    result = []
    lower_heap = []
    higher_heap = []
    for i in sequence:
        if len(lower_heap) == 0:
            heapq.heappush(lower_heap, -i)
            result.append(i)
        else:
            if i <= -lower_heap[0]:
                heapq.heappush(lower_heap, -i)
            else:
                heapq.heappush(higher_heap, i)
            if len(lower_heap) > len(higher_heap) + 1:
                ans = heapq.heappop(lower_heap)
                heapq.heappush(higher_heap, -ans)
            elif len(higher_heap) > len(lower_heap):
                ans = heapq.heappop(higher_heap)
                heapq.heappush(lower_heap, -ans)

            if len(higher_heap) == len(lower_heap):
                result.append((higher_heap[0]-lower_heap[0]) / 2)
            else:
                result.append(-lower_heap[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
