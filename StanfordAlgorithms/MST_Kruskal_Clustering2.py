"""
Difference between any two nodes is the Hamming distance

(The number of ones in bits[u] ^ bits[v])

"""

import queue

class DS():
    def __init__(self, keys):
        self.size = {i:1 for i in keys}             # balancing size is alternative to rank
        self.root = {i:i for i in keys}
        self.clusters = len(keys)

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


def BitClustering(seq, B=None):
    # Would optimize better if using bit operations instead of string

    keys = list(seq.keys())

    ds = DS(keys)
    if B == None:
        B = len(seq[keys[0]])   # length of one bit seq

    for k in keys:
        # Deal with all nodes with Hamming distance 1
        bitseq = list(k)
        diff_by_1 = set()
        for i in range(B):
            neighbor = tuple(bitseq[:i] + [not bitseq[i]] + bitseq[i+1:])
            if neighbor in seq:
                ds.union(k, neighbor)
            diff_by_1.add(neighbor)

        # Deal with all nodes with Hamming distance 2
        diff_by_2 = set()
        for j in range(B):
            for diff in list(diff_by_1):
                diff = list(diff)
                neighbor = tuple(diff[:j] + [not diff[j]] + diff[j+1:])
                if neighbor in seq:
                    ds.union(k, neighbor)
                diff_by_2.add(neighbor)

    return ds.getClusters()



def alg(FNAME):

    with open(FNAME, "r") as fin:
        lines = fin.readlines()
        V, B = [int(x) for x in lines[0].strip().split()]
        edges = queue.PriorityQueue()
        seq = {}
        for i, line in enumerate(lines[1:]):
            bitseq = tuple(bool(int(x)) for x in line.split())
            seq[bitseq] = True  # We actually don't care about identity, only belongingness to cluster!

    res = BitClustering(seq, B)
    # print(res)
    return res

res = alg("3.2large.txt")
print(res)
