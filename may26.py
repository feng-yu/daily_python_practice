"""
[easy]
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def is_unival(root):
    if root.left and root.right:  # both are not empty
        if root.data == root.left.data and root.data == root.right.data and is_unival(root.left) and is_unival(
                root.right):
            return True
        else:
            return False
    elif root.left:  # only has left child
        if root.data == root.left.data and is_unival(root.left):
            return True
        else:
            return False
    elif root.right:  # only has right child
        if root.data == root.right.data and is_unival(root.right):
            return True
        else:  # it's leaf, has no child
            return False
    else:
        return True


def count_unival_tree(root):
    total_count = 0
    if is_unival(root):
        total_count += 1
    total_count = count_unival_tree(root.left) + count_unival_tree(root.right)
    return total_count


def count_unival_helper(root):
    if root is None:
        return 0, True
    left_count, left_is_unival = count_unival_helper(root.left)
    right_count, right_is_unival = count_unival_helper(root.right)
    total_count = left_count + right_count

    if left_is_unival and right_is_unival:
        if root.left and root.data != root.left.data:
            return total_count, False
        if root.right and root.data != root.right.data:
            return total_count, False
        return total_count + 1, True


def count_unival(root):
    count, _ = count_unival_helper(root)
    return count
