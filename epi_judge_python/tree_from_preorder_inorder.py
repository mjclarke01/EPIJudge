from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


# pre-order =>  root, left, right
# in-order => left, root, right
# Overcomplicated - see book
def binary_tree_from_preorder_inorder(preorder, inorder):
    if len(preorder) == 0:
        return None

    lookup = {d: i for i, d in enumerate(inorder)}
    seen = {preorder[0]}

    root = BinaryTreeNode(preorder[0])
    current = root

    for i in range(0, len(preorder) - 1):
        curr_item = lookup[preorder[i]]
        next_item = lookup[preorder[i + 1]]

        if next_item < curr_item:
            # It is left
            node = BinaryTreeNode(preorder[i+1])
            node.parent = current
            current.left = node
            current = node
            seen.add(preorder[i+1])
        else:
            # It is right
            node = BinaryTreeNode(preorder[i + 1])
            node.parent = current
            current.right = node
            current = node
            seen.add(preorder[i + 1])

        if len(seen) == len(inorder):
            break

        next_item += 1
        visit = set(inorder[0:next_item + 1])

        if visit.issubset(seen):
            while True:
                # If the next parent has also been seen then go up to that
                if inorder[next_item + 1] in seen:
                    next_item += 1
                else:
                    break
            # Go up until we hit the node with the same value
            while current.data != inorder[next_item]:
                current = current.parent

    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
