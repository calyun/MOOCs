"""
TSP with Greedy nearest-neighbor heuristic
"""

import math

INF = 88888888

def TSP(coords):

    N = len(coords)
    visited = [False for i in range(N)]

    visited[0] = True
    total_dist = 0

    path = [0]

    for _ in range(N-1):

        closest = None
        min_cost = INF

        for j in range(N):
            if visited[j]:
                continue
            cost = getCost(coords, j, path[-1])

            if cost < min_cost:
                min_cost = cost
                closest = j

        total_dist += math.sqrt(min_cost)
        path.append(closest)
        visited[closest] = True

    total_dist += math.sqrt(getCost(coords, path[-1], path[0]))

    return total_dist



def getCost(coords, j, k):
    """
    Calculates Square of Euclidean distance between two points j, k
    """
    jx, jy = coords[j]
    kx, ky = coords[k]
    return (ky - jy)**2 + (kx - jx)**2


def alg(FNAME):
    with open(FNAME, "r") as fin:
        lines = fin.readlines()

        N = int(lines[0].strip())
        coords = [0 for i in range(N)]

        for i in range(N):
            coords[i] = tuple([float(x.strip()) for x in lines[i+1].split()[1:]])


    res = TSP(coords)
    res = int(res//1)

    return res


print(alg("4.3.txt"))