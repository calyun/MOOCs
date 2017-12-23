"""
Implements O(N^2 * 2^N) algorithms for Travelling Salesman Problem


DEFINE SUBPROBLEMS

Memo will have parameters
m: subproblem size
j: destination vertex
S: set of size m


DEFINE OPTIMAL SUBSTRUCTURE / RECURRENCE RELATION

Looking for /shortest path from 1 to j using only nodes in S/

memo[S, j]
= the minimum for k in S of
memo[S - {j}, k] + cost(k, j)

Final solution:
= the minimum for j from 2 to n of
memo[{all vertices}, j] + cost(j, 1)

{shortest path from 1 to j visiting all vertices} + {cost of final hop}


DEFINE BASE CASES

A[S, 1] = 0 for only S = {1}, +INF otherwise
"""

import copy, math
import matplotlib.pyplot as plt

INF = 88888888

def TravellingSalesman(coords):

    N = len(coords)

    A = {}              # (tuple of S, j)
    distances = [[getCost(coords, j, k) for j in range(N)] for k in range(N)]

    # For subset of single vertex
    new_keys = set()
    for i in range(N):
        S = 1 << (N - i - 1)
        new_keys.add(S)
        for j in range(N):
            A[(S, j)] = INF if i != j else 0

    # For larger sizes of vertex subsets
    for m in range(2, N+1):

        # Generate all subsets of size m
        prev_keys = copy.copy(new_keys)
        new_keys = set()
        for S in prev_keys:
            for i in range(N):
                ibits = 1 << (N - i - 1)
                if not S & ibits:      # if i not in S
                    new_S = S + ibits
                    new_keys.add(new_S)

        # For each set S of size m
        for S in new_keys:

            # Calculate A[S, j] with A[cand_S, k] for k in cand_S
            for j in range(1, N):       # for j in S
                jbits = 1 << (N - j - 1)
                if not S & jbits:
                    continue

                A[(S, j)] = INF
                cand_S = S - jbits
                # print("j {}, cand_S {}".format(j, cand_S))

                for k in range(N):      # for k in S
                    kbits = 1 << (N - k - 1)
                    if k == j or not cand_S & kbits:
                        continue
                    A.setdefault((cand_S, k), INF)
                    A[(S, j)] = min(A[(S, j)], A[(cand_S, k)] + distances[j][k])


    # Calculate length of shortest cycle
    allS = (1 << N) - 1
    result = INF
    for j in range(1, N):
        from_j = A[(allS, j)] + distances[j][0]
        if from_j < result:
            result = from_j

    # Generates path -- not perfect
    curr_S = allS
    path = [0]
    prev = 0

    for _ in range(N-1):

        dist = INF
        for j in range(1, N):

            jbits = 1 << (N - j - 1)
            if not curr_S & jbits:
                continue

            from_j = A[(curr_S, j)] + distances[j][prev]
            if from_j < dist:
                dist = from_j
                prev = j

        path.append(prev)
        prevBits = 1 << (N - prev - 1)
        curr_S -= prevBits

    path.append(0)

    return result, path


def getCost(coords, j, k):
    """
    Calculates Euclidean distance between two points j, k
    """
    jx, jy = coords[j]
    kx, ky = coords[k]
    return math.sqrt((ky - jy)**2 + (kx - jx)**2)



def alg(FNAME):

    with open(FNAME, "r") as fin:
        lines = fin.readlines()
        N = int(lines[0].strip())
        coords = []
        for line in lines[1:]:
            x, y = [float(z.strip()) for z in line.split()]
            coords.append((x, y))

    # res, path = TravellingSalesman(coords, distances)
    # return res

    # Manual modification for particular Coursera assignment file
    THRESHOLD_X = 23800
    THRESHOLD_XR = 24500
    leftCoords = []
    rightCoords = []
    for x, y in coords:
        if x < THRESHOLD_X:
            leftCoords.append((x, y))
        elif x > THRESHOLD_XR:
            rightCoords.append((x, y))
        else:
            leftCoords.append((x, y))
            rightCoords.append((x, y))

    # Visualize points
    labels = ['{0}'.format(i) for i in range(N)]
    coordsX = [pt[0] for pt in coords]
    coordsY = [pt[1] for pt in coords]

    plt.scatter(coordsX, coordsY, s=4)
    for label, x, y in zip(labels, coordsX, coordsY):
        plt.annotate(label, xy=(x, y))
    plt.show()

    resLeft, pathLeft = TravellingSalesman(leftCoords)
    resRight, pathRight = TravellingSalesman(rightCoords)

    def getPathCoords(path, coords):
        pathX = [coords[c][0] for c in path]
        pathY = [coords[c][1] for c in path]
        return pathX, pathY

    leftX, leftY = getPathCoords(pathLeft, leftCoords)
    rightX, rightY = getPathCoords(pathRight, rightCoords)

    plt.plot(leftX, leftY, 'b', rightX, rightY, 'b')
    plt.show()

    # Visually identified commonEdge
    commonEdge = getCost(coords, 11, 12)
    res = resLeft + resRight - 2*commonEdge

    return int(res//1)


print(alg("4.2.txt"))