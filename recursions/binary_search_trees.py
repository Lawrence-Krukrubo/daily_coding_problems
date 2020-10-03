"""
Trees are a recursive data structure because their definition is self-referential.
A tree is a data structure which contains a piece of data and references to other trees!
Trees which are referenced by other trees are known as children. Trees which hold references
to other trees are known as the parents.

A tree can be both parent and child.

Binary search trees:

Reference two children at most per tree node.
1. The “left” child of the tree must contain a value lesser than its parent
2. The “right” child of the tree must contain a value greater than its parent.
3. Trees are an abstract data type, meaning we can implement our version in a number of ways
as long as we follow the rules above.
"""

"""
RECURSIVE STRATEGY

Our high-level strategy before moving through the checkpoints.

base case: the input list is empty
>> Return "No Child" to represent the lack of node

recursive step: the input list must be divided into two halves
>>Find the middle index of the list
>>Store the value located at the middle index
>>Make a tree node with a "data" key set to the value
>>Assign tree node’s "left child" to a recursive call using the left half of the list
>>Assign tree node’s "right child" to a recursive call using the right half of the list
>>Return the tree node
"""


def binary_search_tree(my_list):
    """ Build a binary search tree

    :param my_list: List of numbers
    :return: a dictionary (binary_tree0
    """
    my_list.sort()
    # Base case:
    if not my_list:
        return 'No Child'

    mid_idx = len(my_list) // 2
    mid_value = my_list[mid_idx]

    # Recursive case
    tree_node = {'root_node': mid_value, 'left_child': binary_search_tree(my_list[:mid_idx]),
                 'right_child': binary_search_tree(my_list[mid_idx + 1:])}

    return tree_node


runtime = "N*logN"

if __name__ == '__main__':
    len_odd = [2, 7, 8, 5, 4, 9, 10]
    len_even = [5, 8, 3, 9, 4, 6]

    binary_search_tree = binary_search_tree(len_even)
    print(binary_search_tree)