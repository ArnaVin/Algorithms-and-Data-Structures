# PARTITION: 
# Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions

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

    def partition(self, p):
        pass

l = [3, 5, 8, 5, 10, 2, 1]
test = LinkedList()
for i in l:
    test.insert(i)

test.display()
p = int(input("Enter partition element: "))