from test_framework import generic_test
from collections import deque


def binary_tree_depth_order(tree):
    result = []
    current_q = deque()
    next_q = deque()

    if tree:
        current_q.append(tree)

    while len(current_q) > 0:
        acc = []
        while len(current_q) > 0:
            a = current_q.popleft()
            acc.append(a.data)
            if a.left:
                next_q.append(a.left)
            if a.right:
                next_q.append(a.right)
        current_q, next_q = next_q, current_q
        result.append(acc)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
