from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal(tree):
    def _traverse(root, result):
        if root.left:
            _traverse(root.left, result)
        if root.right:
            _traverse(root.right, result)
        result.append(root.data)

    result = []
    if tree:
        _traverse(tree, result)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))
