from test_framework import generic_test


def sum_root_to_leaf(tree, partial_path_sum=0):
    def _traverse(root, running_sum, results):
        running_sum = (running_sum << 1) + root.data

        if not root.left and not root.right:
            results.append(running_sum)

        if root.left:
            _traverse(root.left, running_sum, results)
        if root.right:
            _traverse(root.right, running_sum, results)

    results = []
    if tree:
        _traverse(tree, 0, results)
    return sum(results)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
