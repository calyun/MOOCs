#Uses python3

import sys
import queue

def distance(adj, cost, s, t):
    
    INF = 99999
    prev = [None for i in range(len(adj))]
    found = [False]*len(adj)
    dists = [INF]*len(adj)
    dists[s] = 0

    while sum(found) != len(adj):
        v = dists.index(max(dists))
        for i in range(len(dists)):
            if not found[i] and dists[i] <= dists[v]:
                v = i
        # v is now min that has not yet shortest-path guarantee
        if v == t:
            break
        found[v] = True
        for i in range(len(adj[v])):
            n = adj[v][i]
            if dists[n] > dists[v] + cost[v][i]:
                dists[n] = dists[v] + cost[v][i]
                prev[n] = v

    if dists[t] == INF:
        return -1
    else:
        return dists[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
