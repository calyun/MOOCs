#!/sh/python3


def Dijkstra(adj, start):
    """
    Time: O(n * m)
    Could be reduced to O(log n * m) with heap implementation
    """

    INF = 99999999
    nodes = list(adj.keys())
    #prev = {i = None for i in nodes}
    visited = {i: None for i in nodes}
    dists = {i: INF for i in nodes}

    dists[start] = 0
    visited_count = 0

    print(adj)

    while visited_count < len(nodes):
        v = max(dists, key=dists.get)
        for i in nodes:
            if not visited[i] and dists[i] <= dists[v]:
                v = i
        # v is now min that has not yet shortest-path guarantee
        visited[v] = True
        visited_count += 1
        for i in range(len(adj[v])):
            n, cost = adj[v][i][0], int(adj[v][i][1])
            if dists[n] > dists[v] + cost:
                dists[n] = dists[v] + cost
                #prev[n] = v

    for i in nodes:
        dists[i] = -1 if dists[i] == INF else dists[i]

    return dists


def evaluate(FNAME):

    # Reads file, creates adjacency list
    adj = {}

    with open(FNAME, "r") as fin:
        lines = fin.readlines()
        for line in lines:
            line = line.split()
            if len(line) < 2:       # invalid line
                continue
            v, n = int(line[0]), line[1:]
            for i in range(len(n)):
                n[i] = tuple([int(x) for x in n[i].split(",")])   # (neighbor, cost)
            adj[v] = n

    start = 1
    targets = [7,37,59,82,99,115,133,165,188,197]
    res = []

    distances = Dijkstra(adj, start)

    for t in targets:
        res.append(distances[t])
    res = ','.join([str(i) for i in res])
    return res


def alg(FNAME):

    res = evaluate(FNAME)
    res = ",".join([str(i) for i in res])
    print(res)
    return res


FNAME = "2.2.in"
res = evaluate(FNAME)
print(res)
