import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree):
    def _traverse(root, result):
        if not root:
            return
        if not root.left and not root.right:
            results.append(root)
        if root.left:
            _traverse(root.left, result)
        if root.right:
            _traverse(root.right, result)

    if not tree:
        return []
    results = [tree]
    if tree.left:
        curr = tree.left
        while curr.left or curr.right:
            results.append(curr)
            curr = curr.left if curr.left else curr.right
    _traverse(tree.left, results)
    _traverse(tree.right, results)

    curr = results[-1].parent if tree.right else None
    while curr:
        if curr.parent:
            results.append(curr)
        curr = curr.parent

    return results


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
