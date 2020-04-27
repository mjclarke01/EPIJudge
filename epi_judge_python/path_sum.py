from test_framework import generic_test


def has_path_sum(tree, remaining_weight):
    def _traverse(root, weight):
        weight -= root.data

        if weight == 0 and root.left is None and root.right is None:
            return True

        if root.left:
            if _traverse(root.left, weight):
                return True
        if root.right:
            if _traverse(root.right, weight):
                return True

        return False

    return _traverse(tree, remaining_weight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("path_sum.py", 'path_sum.tsv',
                                       has_path_sum))
