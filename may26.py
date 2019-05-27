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
import random


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """always try to add as left child"""
        if self.left is None:
            self.left = Node(data)
        elif self.right is None:
            self.right = Node(data)
        else:
            if random.randint(0,1):   #is 0 go to left, otherwise go to right
                self.right.insert(data)
            else:
                self.left.insert(data)

    def print_node(self):
        if self.left:
            self.left.print_node()
        print( self.data)
        if self.right:
            self.right.print_node()


    def __str__(self):
        str_node = ''
        if self.left:
            str_node += str(self.left)
        str_node = str_node + ' ' + str(self.data)
        if self.right:
            str_node = str_node + ' ' + str(self.right)
        return str_node


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

"""
[easy]
Problem:  Given the root to a binary tree, count the total number of nodes there are.
"""
def count_node(root):
    return count_node(root.left) + count_node(root.right) + 1 if root else 0


"""
[easy}
Problem:  Given the root to a binary tree, return the deepest node.
"""
def increment_depth(deepest_tuple):
    node, depth = deepest_tuple
    return node, depth+1


def deepest_node(node):
    if node and not node.left and not node.right:   #leaf
        return node, 1
    if node.left:
        return increment_depth(deepest_node(node.left))
    if node.right:
        return increment_depth(deepest_node(node.right))
    return increment_depth(max(deepest_node(node.left), deepest_node(node.right),
               key=lambda x: x[1]))


def nodetest():
    root = Node(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.insert(5)
    root.insert(6)
    root.insert(7)
    root.insert(8)
    root.insert(9)
    root.insert(10)
    root.print_node()
    print(count_node(root))
    d_node, depth = deepest_node(root)
    print(f'Deepest node has value: {d_node.data} with depth: {depth}')

nodetest()