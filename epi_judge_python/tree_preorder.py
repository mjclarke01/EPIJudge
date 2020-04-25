from test_framework import generic_test
from collections import deque


def preorder_traversal(tree):
    def _traverse(root, result):
        result.append(root.data)
        if root.left:
            _traverse(root.left, result)
        if root.right:
            _traverse(root.right, result)

    result = []
    if tree:
        _traverse(tree, result)
    return result


def preorder_traversal(tree):
    if not tree:
        return []

    result = []
    q = []

    while tree or q:
        if tree:
            result.append(tree.data)
            q.append(tree)
            tree = tree.left
        else:
            tree = q.pop()
            tree = tree.right

    return result


# From the book
def preorder_traversal(tree):
    path, result = [tree], []
    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right, curr.left]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
