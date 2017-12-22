
def KnapsackIterative(items, max_weight):
    """
    Solves knapsack problem in iterative manner

    Time: O(NW)
    Space: O(NW)
    """
    N = len(items)
    # print("Max Weight: {}\nItems: {}".format(max_weight, items))

    memo = [[0 for j in range(N+1)] for i in range(max_weight+1)]

    for i in range(1, N+1):

        # print("At item: {}".format(i))

        value, weight = items[i-1]

        # Update memo for lower-weight entries
        for j in range(weight):
            memo[j][i] = memo[j][i-1]

        # Update memo for higher-weight entries
        for j in range(weight, max_weight+1):
            exclude = memo[j][i-1]
            include = memo[j-weight][i-1] + value
            memo[j][i] = max(exclude, include)

    # printGrid(memo)

    return memo[-1][-1]


def printGrid(grid):

    for r in grid:
        print(r)
    print()


def alg(FNAME):

    with open(FNAME, "r") as fin:
        lines = fin.readlines()
        S, N = [int(x.strip()) for x in lines[0].split()]
        items = [tuple(int(x) for x in line.split()) for line in lines[1:]]

    res = KnapsackIterative(items, S)

    return res


print(alg("3.4small.txt"))
