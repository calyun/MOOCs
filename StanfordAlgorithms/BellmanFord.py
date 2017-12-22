#!/usr/bin/python3

"""
Not used in any assignment here
Copied from UCSD Folder for reference
"""

import sys

# prevents overflow
INF = float('inf')

def BellmanFord(adj, cost, s):

    n_v = len(adj)
    dist = [INF] * n_v
    prev = [i for i in range(n_v)]
    dist[s] = 0

    # Bellman-Ford algorithm O(N^2*D) = O(N*M)
    for i in range(n_v-1):
        for v in range(n_v):
            for j in range(len(adj[v])):
                n = adj[v][j]
                if dist[n] > dist[v]+cost[v][j]:
                    dist[n] = dist[v]+cost[v][j]
                    prev[n] = v

    # Run Bellman-Ford for one more cycle to detect negative cycle.
    # If still shorter shortest paths remain, deal with the negative cycle recursively
    for v in range(n_v):
        for j in range(len(adj[v])):
            n = adj[v][j]
            if dist[n] > dist[v]+cost[v][j]:
                bfs_neg(adj, v, dist)

    return dist


# all nodes reachable from n is also -INF
def bfs_neg(adj, v, dist):

    for n in adj[v]:
        if dist[n] != -INF:
            dist[n] = -INF
            bfs_neg(adj, n, dist)


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
    s = data[0]
    s -= 1
    dist = shortest_paths(adj, cost, s)
    for x in range(n):
        if dist[x] == INF:
            print("*")
        elif dist[x] == -INF:
            print("-")
        else:
            print(dist[x])

