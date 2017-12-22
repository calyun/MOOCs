import sys, random, copy

FNAME = "1.4"
fin = open(FNAME + ".in", "r")
sys.stdin = fin
#fout = open(FNAME + ".out", "w")
#sys.stdout = fout

def minCut(adj):
    """
    Randomized contraction algorithm for min cuts (Karger, 1993)

    """
    adj = copy.deepcopy(adj)

    while len(list(adj.keys())) > 2:
        keys = list(adj.keys())
        u = random.choice(keys)
        v = random.choice(adj[u])
        # merge v into u
        adj[u] += [i for i in adj[v] if i != u and i != v]
        for n in adj[v]:
            adj[n] = [u if i == v else i for i in adj[n] if i != n]
        del adj[v]

    # print(adj)
    keys = list(adj.keys())
    return len(adj[keys[0]])

def readFile():
    lines = fin.readlines()
    adj = {}

    for line in lines:

        line = line.split()
        if len(line) == 0:
            continue

        v, neighbors = line[0], line[1:]
        adj[v] = neighbors
        for n in neighbors:
            adj.setdefault(n, [])
            adj[n].append(v)

    return adj

def run(iterations, step=10):
    adj = readFile()
    results = [minCut(adj)]

    for i in range(iterations):
        trial = minCut(adj)
        if (i % step == 0):
            print(min(results))

    return min(results)


print(run(100))
