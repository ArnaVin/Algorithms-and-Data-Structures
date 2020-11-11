# DELETE MIDDLE NODE: 
# Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, 
# given only access to that node. 

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

    def dmn(self, e):
        temp = self._head
        while temp._nxt._element != e:
            temp = temp._nxt
        temp._nxt = temp._nxt._nxt

l = [1, 2, 3, 4, 5, 6]
test = LinkedList()
for i in l:
    test.insert(i)

test.display()
e = int(input("Which node from above is to be removed: "))
test.dmn(e)
test.display()