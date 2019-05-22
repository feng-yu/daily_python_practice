"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        s = "Node('%s'" % self.val
        if self.left:
            s = s + " %s" % str(self.left)
            if self.right:
                s = s + " %s)" % str(self.right)
        else:
            s = s + ")"
        return s


def serialize(root, level=0):
    if root:
        result = str(root.val)
    if root.left:
        result = result + 'l%i:' % (level) + serialize(root.left, level+1)
    if  root.right:
        result = result + 'r%i:' % (level) + serialize(root.right, level+1)
    return result


def deserialize(string, level=0):
    l_index = string.find('l%i:' % (level))
    if l_index == -1:
        return Node(string)

    r_index = string.find('r%i:' % (level))

    val = string[:l_index]
    if r_index != -1:
        l_str = string[l_index+len('l%i:' % (level)):r_index]
        r_str = string[r_index+len('r%i:' % (level)):]
        if r_str:
            right = deserialize(r_str, level+1)
    else:
        l_str = string[l_index+len('l%i:' % (level)):]
        right = None
    left = deserialize(l_str, level+1)

    return Node(val, left, right)


# node=Node('root')
# node=Node('root', Node('left'))
# node = Node('root', Node('left'), Node('right'))
node =  Node('root', Node('left', Node('left.left')), Node('right'))
# node =  Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))
# node =  Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', Node('right.left'), Node('right.right')))

s = serialize(node)
print(s)
rn = deserialize(s)
print(rn)
assert deserialize(serialize(node)).left.left.val == 'left.left'



