#Uses python3
import sys
import math
import queue

class DisjointSet:
    """
    Weighted, has path compression
    """
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def make_set(self, x):      # makes x its own set
        self.parent[x] = x
        #rank[x] = 0

    def find(self, p):          # find with path compression
        # if p != self.parent[p]:
        #     self.parent[p] = find(self.parent[p])
        while (p != self.parent[p]):
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if self.size[rootP] < self.size[rootQ]:
            # links self.parent of set2 to set1
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]


def minimum_distance(x, y):
    result = 0
    # Kruskal's algorithm
    n_v = len(x)

    X = DisjointSet(n_v)
    E = queue.PriorityQueue()
    # (d, (i, j))

    # sort edges in nondecreasing order of weight
    for i in range(n_v):
        for j in range(n_v):
            if i == j:
                continue
            xd = x[i]-x[j]
            yd = y[i]-y[j]
            d = math.sqrt(xd*xd+yd*yd)
            E.put((d, (i,j)))

    # take the minimum edge in priority queue that crosses a cut
    # (is safe -- minimum and no cycle)
    while not E.empty():
        d, edge = E.get()
        if X.find(edge[0]) != X.find(edge[1]):
            result += d
            X.union(edge[0], edge[1])

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))