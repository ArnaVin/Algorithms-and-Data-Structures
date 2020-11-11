# RETURN Kth TO LAST:
# Implement an algorithm to find the kth to last element of a singly linked list

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

    def ktolast(self, k):
        p1 = self._head
        p2 = self._head

        for _ in range(k):
            if p1 == None: return None
            p1 = p1._nxt
        
        while (p1 != None):
            p1 = p1._nxt
            p2 = p2._nxt
        
        print(f"{k}th to last element is : {p2._element}")

l = [1, 2, 3, 4, 5, 6]
test = LinkedList()
for i in l:
    test.insert(i)

test.display()
k = int(input("Enter Kth to last element: "))
test.ktolast(k)

'''
We use two pointers, p1 and p2. We place them k nodes apart in the linked list by 
putting p2 at the beginning and moving p1 k nodes into the list. Then, when we move 
them at the same pace, p1 will hit the end of the linked list after (LENGTH - k) steps. 
At that point, p2 will be (LENGTH - k) nodes into the list, or k nodes from the end. 

This algorithm takes O(n) time and O(1) space
'''