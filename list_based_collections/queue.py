"""
A Queue, generally has a FIFO mode. First-In-First-Out.
Here, the oldest element, comes out first.
The first in, is the head and the last in, the tail.
Peek is looking at the head, without removing it.
Enqueue is adding an element to the queue,
Dequeue is removing an element from the queue.

A Double-Ended-Queue called deque is a python data structure,
that offers the ability to enqueue and dequeue from both sides.
It acts like a Stack and a Queue together.
We can treat it like a queue and add and remove elements from same end
Or like a Stack and add and remove elements from different ends

A Priority Queue is one where we enqueue elements with a numerical priority,
And when we dequeue we remove elements with the highest or lowest priority as maybe.
This is not like the normal queue where we remove based on the oldest element.
But if the elements have the same priority, than the oldest gets popped first.

<<from collections import deque>>
"""

"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""


class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)


if __name__=='__main__':
    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    # Should be 1
    print(q.peek())

    # Test dequeue
    # Should be 1
    print(q.dequeue())
    # Test enqueue
    q.enqueue(4)
    # Should be 2
    print(q.dequeue())
    # Should be 3
    print(q.dequeue())
    # Should be 4
    print(q.dequeue())
    q.enqueue(5)
    # Should be 5
    print(q.peek())













