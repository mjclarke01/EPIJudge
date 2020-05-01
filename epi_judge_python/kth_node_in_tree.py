import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


# Naive version just to check I understand the problem
def find_kth_node_binary_tree(tree, k):
    s = []

    while s or tree:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            k -= 1
            if k == 0:
                return tree
            tree = tree.right
    return None


# divide and conquer
def find_kth_node_binary_tree(tree, k):
    s = []

    while s or tree:
        if tree and tree.size < k:
            k -= tree.size
            tree = None

        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            k -= 1
            if k == 0:
                return tree
            tree = tree.right
    return None


# Stackless - from the book
def find_kth_node_binary_tree(tree, k):
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k:
            k -= left_size + 1
            tree = tree.right
        elif left_size == k-1:
            return tree
        else:
            tree = tree.left



@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(
        functools.partial(find_kth_node_binary_tree, tree, k))

    if not result:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_node_in_tree.py",
                                       "kth_node_in_tree.tsv",
                                       find_kth_node_binary_tree_wrapper))
