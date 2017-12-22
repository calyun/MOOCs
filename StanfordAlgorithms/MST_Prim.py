# Adapted from MST_Kruskal.py implementation of Kruskal's Algorithm (adapted from HackerRank problem submission)

import queue

class DS():
    def __init__(self, n):
        self.size = [1]*n               # balancing size is alternative to rank
        self.root = [i for i in range(n)]

    def find(self, n):      # Path compression
        while n != self.root[n]:
            self.root[n] = self.root[self.root[n]]
            n = self.root[n]
        return n

    def union(self, p, q):
        p,q = self.root[p], self.root[q]
        if self.size[p] > self.size[q]:
            r1, r2 = p, q
        else:
            r1, r2 = q, p
        self.root[r2] = r1
        self.size[r1] += self.size[r2]
        self.size[r2] = self.size[r1]


def Prim(edges, V):

    # Adds the cheapest edge to start us off
    cost, e = edges.get()
    u, v = e
    X = set([u, v])
    result = cost

    # Adds cheapest neighboring edges until all vertices reached
    while len(X) < V and not edges.empty():
        cost, e = edges.get()
        u, v = e
        otherEdges = []

        # Gets cheapest neighboring edge
        while not (u in X and v not in X) and not (u not in X and v in X) and not edges.empty():
            otherEdges.append((cost, e))
            cost, e = edges.get()
            u, v = e

        result += cost
        X.add(u)
        X.add(v)

        # Return the prospective unused edges
        for edge in otherEdges:
            cost, e = edge
            u, v = e
            if u not in X or v not in X:
                edges.put(edge)

    return result


def alg(FNAME):
    with open(FNAME, "r") as fin:
        lines = fin.readlines()
        V, E = [int(i) for i in lines[0].strip().split()]
        edges = queue.PriorityQueue()
        for line in lines[1:]:
            u, v, cost = [int(i) for i in line.split()]
            edges.put((cost, (u,v)))

    res = Prim(edges, V)
    return res

print(alg("3.1Prim.txt"))