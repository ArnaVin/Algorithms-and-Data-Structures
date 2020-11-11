# SUM LISTS: 
# You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list. 

class LinkedList:

    class _Node:
        __slots__ = '_element', '_nxt'

        def __init__(self, element, nxt):
            self._element = element
            self._nxt = nxt

    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def insert(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            temp = self._head
            while (temp._nxt != None):
                temp = temp._nxt
            temp._nxt = newest
        self._size += 1

    def display(self):
        temp = self._head
        while temp != None:
            print(temp._element, end=" ")
            temp = temp._nxt
        print()


