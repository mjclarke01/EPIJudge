from test_framework import generic_test


def has_path_sum(tree, remaining_weight):
    def _traverse(root, weight):
        if not root.left and not root.right:
            return weight == root.data

        if root.left:
            if _traverse(root.left, weight - root.data):
                return True
        if root.right:
            if _traverse(root.right, weight - root.data):
                return True

        return False

    return _traverse(tree, remaining_weight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("path_sum.py", 'path_sum.tsv',
                                       has_path_sum))
