
def readInput():
    adj = {}
    nodes = set()

    for line in fin.readlines():
        if len(line.split()) < 2:
            continue
        v, n = line.split()
        adj.setdefault(v, [])
        adj.setdefault(n, [])
        adj[v].append(n)
        adj[n].append(v)
        nodes.add(v)
        nodes.add(n)

    return adj, nodes


def SizeConnectedComponents(adj, nodes):
    """
    Finds size of five largest connected components in directed graph
    """

    fiveLargest = [0, 0, 0, 0, 0]

    visited = {}
    for n in nodes:
        visited[n] = False
    coumt = 0

    for i in nodes:
        if not visited[i]:
            size = BFS(adj, visited, i)
            print("Component of size", size, "found")
            if size > fiveLargest[0]:
                fiveLargest[0] = size
                fiveLargest.sort()

    return fiveLargest[::-1]


def BFS(adj, visited, i):

    q = [i]
    size = 0
    while len(q) > 0:
        node = q.pop(0)
        visited[node] = True
        size += 1
        for i in adj[node]:
            if not visited[i]:
                q.append(i)
    return size


def evaluate():
    adj, nodes = readInput()
    res = SizeConnectedComponents(adj, nodes)
    print(res)

evaluate()
