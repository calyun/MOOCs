"""
Implements Floyd-Warshall Algorithm


DEFINE SUBPROBLEMS

Memo will have parameters
i: source vertex
j: destination vertex
k: using only the first k vertices


DEFINE OPTIMAL SUBSTRUCTURE / RECURRENCE RELATION

Looking for shortest cycle-free i-j path P using only nodes in V(k)
Case 1: k not included in P --> memo[i,j,k] = memo[i,j,k-1]
Case 2: k included in P --> memo[i,j,k] = memo[i,k,k-1] + memo[k,j,k-1]

So memo[i,j,k] = min of the two cases


DEFINE BASE CASES

For all i, j in V:
memo[i,j,0] =   0 if i = j
                cost(i,j) if (i,j) is an edge
                +INF if i != j and (i,j) is not an edge


"""

def AllPairsShortestPaths(V, edges):
    """
    N = # vertices (V), M = # edges

    Time: O(N^3)
    Space: O(N^2) (modify implementation to only keep prev and current info for k-dimension to get 2-D list)
    """

    memo = [[[None for k in range(V)] for j in range(V)] for i in range(V)]

    # Initialize with base cases
    for i in range(V):
        for j in range(V):
            if (i, j) in edges:
                memo[i][j][0] = edges[(i, j)]
                if i == j and edges[(i, j)] < 0:
                    return 'NULL'
            elif i == j:
                memo[i][j][0] = 0
            else:
                memo[i][j][0] = 1e8

    shortest_shortest_path = 0

    # Floyd-Warshall Algorithm -- DP
    for k in range(1, V):
        for i in range(V):
            for j in range(V):
                exclude_k = memo[i][j][k-1]
                include_k = memo[i][k][k-1] + memo[k][j][k-1]

                memo[i][j][k] = min(exclude_k, include_k)

                # Negative cycle found
                if i == j and memo[i][j][k] < 0:
                    print("NULL found with i {}, j {}, k {}, val {}".format(i,j,k,memo[i][j][k]))
                    return 'NULL'

                elif k == V-1:
                    shortest_shortest_path = min(memo[i][j][k], shortest_shortest_path)

    return shortest_shortest_path


def alg(FNAME):
    with open(FNAME, "r") as fin:

        lines = fin.readlines()
        V, E = [int(x) for x in lines[0].split()]

        edges = {}
        for line in lines[1:]:
            u, v, w = line.split()
            key = (int(u)-1, int(v)-1)
            edges[key] = min(int(w), edges[key]) if key in edges else int(w)

    res = AllPairsShortestPaths(V, edges)
    return res


print(alg("4.1c.txt"))