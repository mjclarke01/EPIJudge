import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import deque


def lca(tree, node0, node1):
    def _traverse(node, path, ans):
        path.append(node)

        if node == node0:
            ans[0] = path.copy()

        if node == node1:
            ans[1] = path.copy()

        if ans[0] and ans[1]:
            prev = 0
            for i, (a,b) in enumerate(zip(ans[0], ans[1])):
                if a != b:
                    break
                prev = i

            return ans[0][prev]

        if node.left:
            result = _traverse(node.left, path, ans)
            if result:
                return result

        if node.right:
            result = _traverse(node.right, path, ans)
            if result:
                return result
        path.pop()
        return None

    # if node0 == node1:
    #     return node0
    return _traverse(tree, deque(), [None, None])


# Try post-order traversal
def lca(tree, node0, node1):
    def _traverse(root):
        if root == node0 or root == node1:
            return root

        l_ans = _traverse(root.left) if root.left else None
        r_ans = _traverse(root.right) if root.right else None

        if l_ans and r_ans:
            return root
        elif l_ans:
            return l_ans
        elif r_ans:
            return r_ans

        return None

    return _traverse(tree)


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
