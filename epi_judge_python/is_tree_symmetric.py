from test_framework import generic_test


def is_symmetric(tree):
    def _traverse(left_node, right_node):
        if not (left_node and right_node):
            return False
        if left_node.data != right_node.data:
            return False

        if left_node.left and right_node.right:
            l_result = _traverse(left_node.left, right_node.right)
            if not l_result:
                return False
        elif left_node.left != right_node.right:
            return False

        if left_node.right and right_node.left:
            r_result = _traverse(left_node.right, right_node.left)
            if not r_result:
                return False
        elif left_node.right != right_node.left:
            return False

        return True

    if tree is None:
        return True

    if tree.left is None and tree.right is None:
        return True

    return _traverse(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
