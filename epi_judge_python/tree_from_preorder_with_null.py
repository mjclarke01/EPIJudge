import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from binary_tree_node import BinaryTreeNode


# Book does it using recursion.
def reconstruct_preorder(preorder):
    stack = []
    for i in reversed(preorder):
        if i is None:
            stack.append(None)
        else:
            node = BinaryTreeNode(i)
            node.left = stack.pop(-1)
            node.right = stack.pop(-1)
            stack.append(node)

    return stack[0]


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
