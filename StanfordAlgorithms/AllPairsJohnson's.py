"""
Johnson's Algorithm

Time: O(N*M*log N)
Space: O(N + M), or O(N) if you directly modify old edge weights

Techically, Time O(N*M*log M) with Djikstra's implementing using Python heap
(which stores multiple items for any vertex rather than throwing away less prioritized ones)
"""

import sys, copy, queue


INF = 8888888

def BellmanFord(adj, start):

    nodes = list(adj.keys())
    V = len(nodes)

    dist = {i: INF for i in nodes}
    #prev = {i: None for i in nodes}

    dist[start] = 0

    # Bellman-Ford algorithm O(N^2*D) = O(N*M)
    for i in range(V-1):
        for v in nodes:
            for n in adj[v]:
                if dist[n] > dist[v] + adj[v][n]:
                    dist[n] = dist[v] + adj[v][n]
                    #prev[n] = v

    # Run Bellman-Ford for one more cycle to detect negative cycle.
    # If still shorter shortest paths remain, deal with the negative cycle recursively
    for v in nodes:
        for n in adj[v].keys():
            if dist[n] > dist[v] + adj[v][n]:
                print("Error: Negative Cycle Found")
                return 'NULL'

    return dist


def Dijkstra(adj, start):
    """
    Time: O(N * M)
    Could be reduced to O((N + M) * log N) == O(M * log N) with heap implementation

    Heap implementation:
    Heap key for unsetX V is minimum weight of incoming edges to V

    Each time, we pull out the minimum weight vertex V
    and find the shortest path to V
    """

    # Define metavariables. Initialize storage data structures.
    nodes = list(adj.keys())
    V = len(nodes)

    # shortest path guaranteed set
    setX = set()
    dists = {i: INF for i in nodes}
    #prev = {i: None for i in nodes}

    dists[start] = 0


    """# HEAP SETUP"""
    # Initialize Priority Queue
    q = queue.PriorityQueue()   # aka V-X
    v_key = {v: (INF, None) for v in nodes}

    # Inducting our first member of X!
    v = start
    setX.add(v)
    # Use smallest weight of incoming edge as key
    for n in adj[v].keys():
        cost = adj[v][n]
        v_key[n] = (cost, v)       # (weight, source)
        item = (v_key[n][0], v_key[n][1], n)
        q.put(item)

    # Iteratively add all edges to X (setX)
    for _ in range(V-1):

        """# HEAP EXTRACT"""
        # Pick V with smallest weight, that doesn't yet have shortest-path guarantee (not in X)
        while v in setX:
            if q.empty():
                return dists
            _, source, v = q.get()

        dists[v] = dists[source] + adj[source][v]

        # Update outgoing edge weights
        for n in adj[v].keys():
            cost = adj[v][n]
            if dists[v] + cost < dists[n]:
                dists[n] = dists[v] + cost
                #prev[n] = v

        """# HEAP UPDATE"""
        # Because we add v to X, we must update all V left in heap
        setX.add(v)
        # Inconveniently, Python heap does not allow us to extract given items.
        # Workaround: Simply add the new shortest path for V and we ignore the lower-priority items for V in Heap Extract step
        # ==> tradeoff of O(M) space for heap instead of O(N) ==> O(M * log M) time
        for n in adj[v].keys():
            cost = adj[v][n]
            if cost < v_key[n][0]:
                v_key[n] = (cost, v)
                item = (v_key[n][0], v_key[n][1], n)
                q.put(item)

    return dists


def Johnson(adj):
    """
    Johnson's Algorithm :D
    """

    # Construct G' by adding S, a vertex with edge with weight 0 to all other vertexes
    nodes = list(adj.keys())
    adj['S'] = {n: 0 for n in nodes}

    # Run Bellman-Ford on G', obtaining shortest paths for each vertex
    distFromS = BellmanFord(adj, 'S')
    if distFromS == 'NULL':
        return 'NULL'
    del adj['S']

    # Modify each edge c' = c + dist[u] - dist[v]
    m_adj = copy.deepcopy(adj)
    for v in nodes:
        for n in adj[v].keys():
            m_adj[v][n] = adj[v][n] + distFromS[v] - distFromS[n]

    # Run Dijkstra's Algorithm on each vertex
    dists = {}
    for v in nodes:
        dists[v] = Dijkstra(m_adj, v)

    # Convert all distances d' to d
    for v in dists.keys():
        for t in dists[v].keys():
            dists[v][t] = dists[v][t] - distFromS[v] + distFromS[t]

    return dists


def alg(FNAME):
    with open(FNAME, "r") as fin:

        lines = fin.readlines()
        V, E = [int(x) for x in lines[0].split()]

        adj = {}
        for line in lines[1:]:
            u, v, w = [int(x) for x in line.split()]
            adj.setdefault(u, {})
            adj.setdefault(v, {})
            adj[u].setdefault(v, w)
            adj[u][v] = min(w, adj[u][v])

    dists = Johnson(adj)

    # Coursera-desired output for detection of negative cycles
    if dists == 'NULL':
        return 'NULL'

    # Coursera assignment-specific
    shortest_shortest = 0
    for v in dists.keys():
        for t in dists[v].keys():
            shortest_shortest = min(shortest_shortest, dists[v][t])
    return shortest_shortest


print(alg("4.1c.txt"))