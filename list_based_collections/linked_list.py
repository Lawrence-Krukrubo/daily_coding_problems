# First define an element class
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# Next a linked-list class


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    """
    This code is very similar—we're just establishing that a LinkedList is something 
    that has a head Element, which is the first element in the list. If we establish 
    a new LinkedList without a head, it will default to None.

    Great! Let's add a method to our LinkedList to make it a little more useful. 
    This method will add a new Element to the end of our LinkedList.
    """

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    """ 
    Again, this part is really important, If the LinkedList already 
    has a head, iterate through the next reference in every Element until you reach 
    the end of the list. Set next for the end of the list to be the new_element. 
    Alternatively, if there is no head already, you should just assign new_element 
    to it and do nothing else.
    
    Next, add 3 methods:- 
        " 1. get_position" returns the element at a certain position.
        " 2. insert" function will add an element to a particular spot in the list.
        " 3. delete" will delete the first element with that particular value.
    """

    def get_position(self, position):
        """ Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        try:
            assert position >= 1
        except AssertionError:
            return None

        counter = 1
        current = self.head

        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1

        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        if position > 1:
            try:
                element_after = self.get_position(position)
                assert element_after is not None
                element_before = self.get_position(position-1)
            except AssertionError:
                return None

            element_before.next = new_element
            new_element.next = element_after

        else:
            element_after = self.get_position(position)
            new_element.next = element_after
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        try:
            assert self.head is not None
        except AssertionError:
            return None

        current = self.head
        counter = 1

        if current.value == value:
            self.head = current.next
            counter += 1

        elif counter == 1:
            found = False
            while current:
                counter += 1
                if current.next.value == value:
                    found += 1
                    break
                current = current.next

            if found:
                del_node = self.get_position(counter)
                base_node = self.get_position(counter-1)
                base_node.next = del_node.next

    """Add a couple methods to our LinkedList class,
    and use that to implement a Stack.
    I have 2 functions below to fill in:
    insert_first, delete_first
    """
    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"

        current = self.head
        self.head = new_element
        new_element.next = current

    def delete_first(self):
        "Delete the first (head) element in the LinkedList and return it"

        current = self.head
        if current:
            self.head = current.next

        return current


if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    print(ll.head.next.next.value)
    # Should also print 3
    print(ll.get_position(3).value)

    # Test insert
    ll.insert(e4, 3)
    # Should print 4 now
    print(ll.get_position(3).value)

    # Test delete
    ll.delete(1)
    # Should print 2 now
    print(ll.get_position(1).value)
    # Should print 4 now
    print(ll.get_position(2).value)
    # Should print 3 now
    print(ll.get_position(3).value)