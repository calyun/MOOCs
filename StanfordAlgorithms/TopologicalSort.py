#!/usr/bin/python3

"""
Not used in any assignment here
Copied from UCSD Assignment Folder for reference
"""

import sys

# Time: ~ V + E
# Space: ~ 2V

def dfs(adj, used, order, x):
    used[x] = True
    for n in adj[x]:
        if not used[n]:
            dfs(adj, used, order, n)
    order.append(x)

def toposort(adj):
    """
    Applications of topological sort include:
	- finding order given dependencies
	(e.g. we can interpret incoming nodes as dependencies)
    Sink nodes are done visiting first.
    By returning sink nodes (most incoming nodes / dependencies) at the end, we ensure the dependencies are accounted for.
    """
    used = [False] * len(adj)
    order = []
    # do DFS
    for v in range(len(adj)):
        if not used[v]:
            dfs(adj, used, order, v)
    # returns iterator, in reverse post-order
    return reversed(order)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
    print();
