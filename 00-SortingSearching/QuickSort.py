import LinkedQueue

def quick_sort(S):

    if len(S) < 2:
        return
    
    p = S.first()               # pivot
    L = LinkedQueue.LinkedQueue()
    E = LinkedQueue.LinkedQueue()
    G = LinkedQueue.LinkedQueue()

    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    quick_sort(L)
    quick_sort(G)
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

test_list = [0, 17, 3, 2, 98, 16, 8, 23]
test = LinkedQueue.LinkedQueue()
for i in test_list:
    test.enqueue(i)

test.display()
quick_sort(test)
print("\n[QUICK SORT] ...")
test.display()