import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def find_depth(node):
        count = 0
        while node.parent:
            count += 1
            node = node.parent
        return count

    n0d = find_depth(node0)
    n1d = find_depth(node1)

    if n0d > n1d:
        node0, node1 = node1, node0
        n0d, n1d = n1d, n0d

    while node0 != node1:
        if n1d > n0d:
            node1 = node1.parent
            n1d -= 1
        else:
            node0 = node0.parent
            node1 = node1.parent

    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
