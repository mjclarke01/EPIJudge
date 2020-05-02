from test_framework import generic_test


def inorder_traversal(tree):
    def _traverse(root, result):
        if root.left:
            _traverse(root.left, result)
        result.append(root.data)
        if root.right:
            _traverse(root.right, result)

    result = []
    if tree:
        _traverse(tree, result)
    return result


# Without recursion - my version
# Better version available on pg 131
def inorder_traversal(tree):
    result = []
    stack = []
    curr = tree
    while curr or stack:
        if curr is None:
            curr = stack.pop()
            result.append(curr.data)
            curr = curr.right
            continue

        if curr.left:
            stack.append(curr)
            curr = curr.left
        else:
            # As far left as we can go
            result.append(curr.data)
            # So go right
            curr = curr.right

    return result


# Stack-less
def inorder_traversal(tree):
    result = []

    prev = None
    while tree:
        if tree.right and tree.right == prev:
            prev = tree
            tree = tree.parent
        elif tree.left and tree.left != prev:
            tree = tree.left
        else:
            result.append(tree.data)
            prev = tree
            tree = tree.right if tree.right else tree.parent

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
