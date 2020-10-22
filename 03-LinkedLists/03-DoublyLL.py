# DOUBLY LINKED LIST

class _DoublyLinkedBase:
# base class providing a DLL representation
    class _Node:
    # lightweight, nonpublic class for storing a doubly linked node
        __slots__ = '_element', '_prv', '_nxt'

        def __init__(self, element, prv, nxt):
            self._element = element
            self._prv = prv
            self._nxt = nxt

    def __init__(self):
    # create an empty list
        self._header = self._Node(None, None, None)
        self._trailer =  self._Node(None, None, None)
        self._header._nxt = self._trailer
        self._trailer._prv = self._header
        self._size = 0

    def __len__(self):
    # returns the number of elements in the list
        return self._size

    def _inset_btw(self, e, predecessor, successor):
    # add an element btw two existing nodes and return new node
        newest = self._Node(e, predecessor, successor)
        predecessor._nxt = newest
        successor._prv = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
    # deletes nonsentinel node from the list and return its element
        predecessor = node._prv
        successor = node._nxt
        predecessor._nxt = successor
        successor._prv = predecessor
        self._size -= 1
        element = node._element
        node._prv = node._nxt = node._element = None
        return element
