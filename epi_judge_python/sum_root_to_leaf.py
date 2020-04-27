from test_framework import generic_test


def sum_root_to_leaf(tree, partial_path_sum=0):
    def _traverse(root, running_sum):
        if not root:
            return 0

        running_sum = (running_sum << 1) + root.data

        if not root.left and not root.right:
            return running_sum

        return _traverse(root.left, running_sum) + _traverse(root.right, running_sum)

    return _traverse(tree, 0)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", "sum_root_to_leaf.tsv", sum_root_to_leaf
        )
    )
