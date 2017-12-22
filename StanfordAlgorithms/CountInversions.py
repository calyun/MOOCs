import sys

FNAME = "1.2"
fin = open(FNAME + ".in", "r")
sys.stdin = fin
#fout = open(FNAME + ".out", "w")
#sys.stdout = fout

def countInversions(a):
    """
    Input: Array of DISTINCT integers

    Output: Merge-sorted version of a
            # inversions in a


    Uses Divide and Conquer to count number of inversions in an array.
    Sorts array and merges the sorted halves to uncover inversions.
    """

    # Base case
    if len(a) == 1:
        return a, 0

    part = len(a)//2

    b, b_inv = countInversions(a[:part])
    c, c_inv = countInversions(a[part:])
    sorted_a, split_inv = mergeAndCount(b, c)

    return sorted_a, b_inv + c_inv + split_inv


def mergeAndCount(b, c):
    """
    Merge-sorts and counts inversions for array of DISTINCT integers

    """

    size_b = len(b)
    size_c = len(c)
    res = [0]*(size_b + size_c)
    split_inv = 0

    # Performs Merge sort, also counts inversions
    i, j, k = 0, 0, 0
    while i < size_b and j < size_c:
        if b[i] <= c[j]:
            res[k] = b[i]
            i += 1
            k += 1
        else:
            split_inv += size_b - i
            res[k] = c[j]
            j += 1
            k += 1

    while i < size_b:
        res[k] = b[i]
        i += 1
        k += 1
    while j < size_c:
        res[k] = c[j]
        j += 1
        k += 1

    return res, split_inv


a = []
for i in range(100000):
    item = int(input())
    a.append(item)

_, res = countInversions(a)
print(res)

