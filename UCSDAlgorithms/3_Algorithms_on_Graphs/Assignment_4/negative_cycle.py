#Uses python3

import sys


def negative_cycle(adj, cost):
    INF = 99999

    num_v = len(adj)
    dists = [INF]*num_v
    dists[s] = 0

    # Bellman-Ford
    for i in range(num_v-1):
        for v in range(num_v):
            for j in range(len(adj[v])):
                n = adj[v][j]
                if dists[n] > dists[v] + cost[v][j]:
                    dists[n] = dists[v] + cost[v][j]

    for v in range(num_v):
        for j in range(len(adj[v])):
            n = adj[v][j]
            if dists[n] > dists[v] + cost[v][j]:
                return 1
    return 0




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
    print(negative_cycle(adj, cost))
