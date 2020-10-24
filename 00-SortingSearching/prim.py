from dataclasses import dataclass, field

@dataclass(eq=False)
class Node :
    idnum : int

@dataclass
class Graph :
    source  : int
    adjlist : dict

    def PrimsMST(self):

        priority_queue = { Node(self.source) : 0 }
        added = [False] * len(self.adjlist)
        min_span_tree_cost = 0

        while priority_queue :

            node = min(priority_queue, key=priority_queue.get)
            cost = priority_queue[node]

            del priority_queue[node]

            if added[node.idnum] == False :
                min_span_tree_cost += cost
                added[node.idnum] = True
                print("Added Node : " + str(node.idnum) + ", cost now : "+str(min_span_tree_cost))

                for item in self.adjlist[node.idnum] :
                    adjnode = item[0]
                    adjcost = item[1]
                    if added[adjnode] == False :
                        priority_queue[Node(adjnode)] = adjcost

        return min_span_tree_cost

if __name__ == "__main__" :
    
    g1_edges_from_node = {}
    g1_edges_from_node[0] = [ (1,1), (2,2), (3,1), (4,1), (5,2), (6,1) ]
    g1_edges_from_node[1] = [ (0,1), (2,2), (6,2) ]
    g1_edges_from_node[2] = [ (0,2), (1,2), (3,1) ]
    g1_edges_from_node[3] = [ (0,1), (2,1), (4,2) ]
    g1_edges_from_node[4] = [ (0,1), (3,2), (5,2) ]
    g1_edges_from_node[5] = [ (0,2), (4,2), (6,1) ]
    g1_edges_from_node[6] = [ (0,1), (2,2), (5,1) ]

    g1 = Graph(0, g1_edges_from_node)
    cost = g1.PrimsMST()
    print("Cost of the minimum spanning tree in graph 1 : " + str(cost) +"\n")
    
"""
We initially perform n insertions into Q, later perform n extract-min operations,
and may update a total of m priorities as part of the algorithm. Those steps are
the primary contributions to the overall running time. With a heap-based priority
queue, each operation runs in O(logn) time, and the overall time for the algorithm
is O((n + m)logn), which is O(mlogn) for a connected graph. Alternatively, we
can achieve O(n2) running time by using an unsorted list as a priority queue.
"""