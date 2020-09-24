from list_based_collections.linked_list import Element, LinkedList

"""
Craeate a stack class that has methods push, and pop.
This stck module has imported Element and Linkedlist,
From the linked_list module, so can be used within.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?
"""

"""
Stacks use a LIFO queue, meaning the Last-In-First-Out
The last element inserted is the first to be popped out.
"""


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()


if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)