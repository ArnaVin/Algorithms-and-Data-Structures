# REMOVE DUPS
# Write a code to remove duplicates from an unsorted linked list

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

    def remove_dups(self):
        current = self._head
        while current != None:
            runner = current
            while runner._nxt != None:
                if runner._nxt._element == current._element:
                    runner._nxt = runner._nxt._nxt
                else:
                    runner = runner._nxt
            current = current._nxt

l = [2, 4, 6, 2, 5, 5]
test = LinkedList()
for i in l:
    test.insert(i)

test.display()
test.remove_dups()
test.display()

'''
we iterate with two pointers: current which iterates through the linked list,
and runner which checks all subsequent nodes for duplicates. 

runs in O(1) space, but 0 (N2) time
'''