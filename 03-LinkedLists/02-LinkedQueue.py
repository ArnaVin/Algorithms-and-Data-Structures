# FIFO Queue implementation using singly linked list

class LinkedQueue:

    class _Node:
    # lightweight, nonpublic class for storing a singly linked list
        __slots__ = '_element', '_nxt'

        def __init__(self, element, nxt):
            self._element = element         # reference to user's element
            self._nxt = nxt                 # reference to next node

    def __init__(self):
    # create an empty queue
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
    # return the number of elements in the queue
        return self._size

    def is_empty(self):
    # return True if the queue is empty
        return self._size == 0

    def first(self):
    # return (but do not remove) the element at the front of he queue
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self._head._element

    def dequeue(self):
    # remove and return the forst element of the queue
        if self.is_empty():
            raise ValueError('Queue is empty')
        answer = self._head._element
        self._head = self._head._nxt
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
    # add an element at the end of the queue
        newest = self._Node(e,None)         # new tail node
        if self.is_empty():
            self._head = newest
        else:
            self._tail._nxt = newest
        self._tail = newest
        self._size += 1

    def display(self):
    # display all elements of the queue
        temp = self._head
        while temp != self._tail:
            print(temp._element, end=" ")
            temp = temp._nxt
        print(self._tail._element)
if __name__ == "__main__":

    test = LinkedQueue()
    print('Is queue empty: ', test.is_empty())
    print('Length of queue: ', len(test))

    test.enqueue(10)
    test.enqueue(15)
    test.enqueue(23)

    print('\nIs queue empty: ', test.is_empty())
    print('Length of queue: ', len(test))
    print('firstmost element in the queue: ', test.first())
    print('Removed element: ', test.dequeue())

    print('\nIs queue empty: ', test.is_empty())
    print('Length of queue: ', len(test))
    print('firstmost element in the queue: ', test.first())
    print('Removed element: ', test.dequeue())

    print('\nIs queue empty: ', test.is_empty())
    print('Length of queue: ', len(test))
    print('firstmost element in the queue: ', test.first())
    print('Removed element: ', test.dequeue())

    print('\nIs queue empty: ', test.is_empty())
    print('Length of queue: ', len(test))

'''
OPERATION    | RUNNING TIME
-------------|-------------
S.enqueue(e) |     O(1)
S.dequeue()  |     O(1)
S.first()    |     O(1)
len(S)       |     O(1)
S.is_empty   |     O(1)

'''