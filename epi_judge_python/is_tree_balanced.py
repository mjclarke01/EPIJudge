from test_framework import generic_test


def is_balanced_binary_tree(tree):
    def _traverse(root, height):
        left = right = height + 1
        balanced = True

        if root.left:
            left, l_balanced = _traverse(root.left, left)
            balanced &= l_balanced
        if root.right:
            right, r_balanced = _traverse(root.right, right)
            balanced &= r_balanced
        if abs(left - right) > 1 or not balanced:
            return 0, False

        return max(left, right), True

    if tree is None:
        return True

    return _traverse(tree, 0)[1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
