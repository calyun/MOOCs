# Alternative implementation: /Coursera/UCSDAlgorithms/3_Algorithms_on_Graphs/Assignment_2/strongly_connected.py

def readInput(FNAME):
    """
    Reads input from file.
    Output:
        adj: {key: [outgoing edges] [incoming edges]}
    """
    fin = open(FNAME, "r")

    adj = {}

    for line in fin.readlines():
        if len(line.split()) < 2:
            continue
        v, n = [int(i) for i in line.split()]
        adj.setdefault(v, [[],[]])
        adj.setdefault(n, [[],[]])
        adj[v][0].append(n)         # outgoing v --> n
        adj[n][1].append(v)         # incoming n <-- v

    fin.close()

    return adj


def reset():
    global visited, fin_order, size, largest_five

    visited = {}
    fin_order = []
    size = 0
    largest_five = [0, 0, 0, 0, 0]


def DFS_Loop(adj, firstLoop):
    """
    Loops through entire graph and executes DFS
    """
    global visited, fin_order, size, largest_five
    for i in list(adj.keys()):
        visited[i] = False

    # Determines order for processing nodes
    if firstLoop:
        nodes = list(adj.keys())[::-1]
    else:
        nodes = fin_order[::-1]

    # Loops through nodes and runs DFS on them
    for i in nodes:
        if not visited[i]:
            DFS(adj, i, firstLoop)

            # Keeps track of component size
            if not firstLoop:
                if size > largest_five[0]:
                    largest_five[0] = size
                    largest_five.sort()
                size = 0

    return


def DFS(adj, i, firstLoop):
    """
    Runs DFS
    """
    global t, visited, fin_order, size, largest_five

    # Runs DFS on Reversed or Standard graph
    out = 1 if firstLoop else 0

    st = [i]
    size = 1
    visited[i] = True

    # Iterative DFS
    while len(st) > 0:
        i = st.pop()
        for j in adj[i][out]:
            if not visited[j]:
                st.append(j)
                visited[j] = True

                if firstLoop:
                    fin_order.append(j)
                else:
                    size += 1

    if firstLoop:
        fin_order.append(i)

    return


def SCC(FNAME):
    """
    Finds size of five largest strongly connected components
    """
    global t, visited, fin_order, size, largest_five

    reset()
    adj = readInput(FNAME)
    DFS_Loop(adj, firstLoop = True)
    DFS_Loop(adj, firstLoop = False)
    res = largest_five[::-1]

    return res


FNAME = "2.1.in"
res = SCC(FNAME)
res = ",".join([str(i) for i in res])
print(res)


def alg(FNAME):
    print(FNAME)
    res = SCC(FNAME)
    res = ",".join([str(i) for i in res])
    print(res)
    return res

