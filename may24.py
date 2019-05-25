"""
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer
and dereference_pointer functions that converts between nodes and memory addresses.

No way to verify the solution, since python has no pointers
"""
class XorLinkedListNode:
    def __init(self, value, both):
        self.value = value
        self.both = both

    def get_pointer(self):
        pass

    @staticmethod
    def derederence_pointer(pointer):
        pass


class XorLinkedList:
    """
    For the first node, the both = bin(0) ^ bin(256)
    """
    def __init__(self, fNode):
        self.first_node = fNode

    def add(self, node):
        current_node_pointer = self.first.get_pointer()
        next_node_pointer = self.first_node.both
        if not next_node_pointer: #there are more than 1 node in the list
            next_node = XorLinkedListNode.derederence_pointer(next_node_pointer)
            while next_node.both != current_node_pointer:
                next_next_node_pointer = next_node.both ^ current_node_pointer
                current_node_pointer = next_node.get_pointer()
                next_node = XorLinkedListNode.derederence_pointer(next_next_node_pointer)
            node.both = current_node_pointer
            next_node.both = next_node.both ^ node.get_pointer
            #TODO add more function here
        else: #there is only one node in the list
            pointer = node.get_pointer()
            self.first.both = pointer
            node.both = self.first.get_pointer()

    def get(self, index):
        current_node = self.first_node
        previous_node_pointer = bin(0)
        if current_node:  #there is at least one node in the list
            current_both = current_node.both
            if not current_both:  #there is only one node in the list
                if index == 0:
                    return current_node
                else:
                    return None
            else:  #there is more than one node in the list
                for i in range(index):
                    next_node_pointer = current_both ^ previous_node_pointer
                    previous_node_pointer = current_node.get_pointer()
                    current_node = XorLinkedListNode.derederence_pointer(next_node_pointer)
                    current_both = current_node.both
                    if current_both == previous_node_pointer:  #reach the end
                        if i != index-1:
                            return None
                return current_node
        else: # empty list
            return None


def byte_test():
    a = 3
    b = 5

    print(f'a={a}:{bin(a)}, b={b}:{bin(b)}')

    c = 0
    c = a ^ b ^ a
    print(f'c={c}:{bin(c)}')

byte_test()

