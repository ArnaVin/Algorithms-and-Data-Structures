# LIFO STACK IMPLENTATION USING A SINGLY LINKED LIST

class LinkedStack:

    class _Node:
    # lightweight, nonpublic class for storing a singly linked node
        __slots__ = '_element', '_nxt'

        def __init__(self, element, nxt):
            self._element = element         # reference to user's element
            self._nxt = nxt                 # reference to next node

    def __init__(self):
    # create an empty stack
        self._head = None                   # reference to the head node
        self._size = 0                      # number of stack elements

    def __len__(self):
    # return thenumber of elements in the stack
        return self._size

    def is_empty(self):
    # return True if the stack is empty
        return self._size == 0

    def push(self, e):
    # add an element to the top of the stack
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
    # return (but do not remove) the element at the top of the stack
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._head._element

    def pop(self):
    # remove and return the element from top of the stack
        if self.is_empty():
            raise ValueError('Stack is empty')
        answer = self._head._element
        self._head = self._head._nxt        # bypass the former top node
        self._size -= 1
        return answer

if __name__ == "__main__":

    test = LinkedStack()
    print('Is stack empty: ', test.is_empty())
    print('Length of stack: ', len(test))

    test.push(10)
    test.push(15)
    test.push(23)

    print('\nIs stack empty: ', test.is_empty())
    print('Length of stack: ', len(test))
    print('Topmost element in the stack: ', test.top())
    print('Removed element: ', test.pop())

    print('\nIs stack empty: ', test.is_empty())
    print('Length of stack: ', len(test))
    print('Topmost element in the stack: ', test.top())
    print('Removed element: ', test.pop())

    print('\nIs stack empty: ', test.is_empty())
    print('Length of stack: ', len(test))
    print('Topmost element in the stack: ', test.top())
    print('Removed element: ', test.pop())

    print('\nIs stack empty: ', test.is_empty())
    print('Length of stack: ', len(test))

'''
OPERATION   | RUNNING TIME
------------|-------------
S.push(e)   |     O(1)
S.pop()     |     O(1)
S.top()     |     O(1)
len(S)      |     O(1)
S.is_empty  |     O(1)

'''