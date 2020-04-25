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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
