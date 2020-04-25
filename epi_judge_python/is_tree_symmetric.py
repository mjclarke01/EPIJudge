from test_framework import generic_test


def is_symmetric(tree):
    def _traverse(left_node, right_node):
        if left_node is None and right_node is None:
            return True
        elif left_node is None or right_node is None:
            return False

        if left_node.data != right_node.data:
            return False

        next_pairs = [
            (left_node.left, right_node.right),
            (right_node.left, left_node.right),
        ]

        for left, right in next_pairs:
            if not _traverse(left, right):
                return False

        return True

    if tree is None:
        return True

    return _traverse(tree.left, tree.right)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_tree_symmetric.py", "is_tree_symmetric.tsv", is_symmetric
        )
    )
