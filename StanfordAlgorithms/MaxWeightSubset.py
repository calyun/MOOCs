
def MaxWeightSubset(weights):
    """
    Input: List of weights

    Output: a subset of NONADJACENT indices with the maximum weight
    """
    N = len(weights)
    prev = [None for i in range(N)]     # (Previous index)
    mx = [None for i in range(N)]       # (Max Weight Thus Far, Whether This Index is Included)

    for i, w in enumerate(weights):
        if i == 0:
            mx[i] = (w, True)
            prev[i] = i
            continue
        elif i == 1:
            mx[i] = (w, True) if w > mx[i-1][0] else (mx[i-1][0], False)
            prev[i] = i if w > mx[i-1][0] else i-1
            continue

        if mx[i-1][0] > mx[i-2][0] + w:       # Exclude this index
            prev[i] = i-1
            mx[i] = (mx[i-1][0], False)
        elif mx[i-1][0] < mx[i-2][0] + w:     # Include this index
            prev[i] = i-2
            mx[i] = (mx[i-2][0] + w, True)
        else:
            print("Error: No ties allowed")


"""
Alternative Reconstruction Algorithm
* Simpler (less cluttered notation + logic), faster, space efficient
* Replaces need for prev list, tuples in mx

    indices = []
    i = len(N) - 1
    while i >= 1:
        if mx[i-1] >= mx[i-2] + weights[i]:
            i -= 1
        else:
            indices.append(i)
            i -= 2

    return indices
"""


    indices = []
    i = N-1 if mx[-1][0] > mx[-2][0] else N-2

    # Checks if included
    if mx[i-1][0] < mx[i-2][0] + w:
        indices.append(i)

    while prev[i] != i:
        if mx[prev[i]][1] == True:
            indices.append(prev[i])
        i = prev[i]

    # print("Weights: {}\nMax: {}\nPrev: {}\nIndices: {}\n".format(weights, mx, prev, indices))

    return indices


def alg(FNAME):

    with open(FNAME, "r") as fin:
        lines = fin.readlines()
        N = int(lines[0].strip())
        weights = [int(x.strip()) for x in lines[1:]]

    indices = MaxWeightSubset(weights)
    indices = set(indices)

    targets = [1, 2, 3, 4, 17, 117, 517, 997]

    for i in range(len(targets)):
        if targets[i]-1 in indices:
            targets[i] = '1'
        else:
            targets[i] = '0'

    res = ''.join(targets)
    return res


print(alg("3.3MaxWeight.txt"))
