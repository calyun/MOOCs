# Implementation of Kruskal's Algorithm (adapted from HackerRank problem submission)

import queue

class DS():
    def __init__(self, V):
        self.size = {i:1 for i in range(1, V+1)}             # balancing size is alternative to rank
        self.root = {i:i for i in range(1, V+1)}
        self.clusters = V

    def find(self, n):      # Path compression by halving
        while n != self.root[n]:
            self.root[n] = self.root[self.root[n]]
            n = self.root[n]
        return n

    def union(self, p, q):
        p,q = self.find(p), self.find(q)
        if p == q:
            return
        if self.size[p] > self.size[q]:
            r1, r2 = p, q
        else:
            r1, r2 = q, p
        self.root[r2] = r1
        self.size[r1] += self.size[r2]
        self.size[r2] = self.size[r1]
        self.reduceClusters()

    def reduceClusters(self):
        self.clusters -= 1

    def getClusters(self):
        return self.clusters


def alg(FNAME):
    with open(FNAME, "r") as fin:
        lines = fin.readlines()
        V = int(lines[0].strip())
        edges = queue.PriorityQueue()
        for line in lines[1:]:
            u, v, cost = [int(i) for i in line.split()]
            edges.put((cost, (u,v)))

    res = KruskalClustering(edges, V)
    # print(res)
    return res


def KruskalClustering(edges, V):

    K = 4
    ds = DS(V)

    # Finds V-K edges and uses Union-Find to result in K clusters
    for _ in range(V-K):
        if edges.empty():
            print('error, too few edges -- invalid edges given')
            break
        cost, edge = edges.get()
        u, v = edge
        # Finds cheapest edge which doesn't result in cycles
        while not edges.empty() and ds.find(u) == ds.find(v):
            cost, edge = edges.get()
            u, v = edge
        ds.union(u, v)

    # Spacing of the optimal K-clustering found is next edge between two clusters
    while ds.find(u) == ds.find(v):
        cost, edge = edges.get()
        u, v = edge

    return cost


res = alg("3.2small.txt")
print(res)
