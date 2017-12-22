import sys, random, statistics, math

FNAME = "1.3"
fin = open(FNAME + ".in", "r")
sys.stdin = fin
#fout = open(FNAME + ".out", "w")
#sys.stdout = fout

def alg(FNAME):
    fin = open(FNAME, "r")
    test_input = fin.readlines()
    results = []

    global num_comp
    num_comp = 0
    test_output1 = quickSort1(test_input[:])
    results.append(num_comp)

    num_comp = 0
    test_output2 = quickSort2(test_input[:])
    results.append(num_comp)

    num_comp = 0
    test_output3 = quickSort3(test_input[:])
    results.append(num_comp)

    return results


def quickSort(A, MODE):
    """
    Input:      A: unsorted array
    Returns:    num_comp: # comparisons
                A: sorted A
    """
    # Base case
    if len(A) <= 1:
        return A

    if MODE == "FIRST":
        pivotIndex = 0
    elif MODE == "LAST":
        pivotIndex = len(A) - 1
    elif MODE == "MEDIAN":
        median = A[math.ceil(len(A)/2)-1]
        first = A[0]
        last = A[-1]
        choices = [first, median, last]
        #print(A)
        #print("choices:", choices)
        pivot_value = sorted(choices)[1]
        if pivot_value == first:
            pivotIndex = 0
        elif pivot_value == median:
            pivotIndex = len(A)//2
        else:
            pivotIndex = len(A) - 1
    else:
        pivotIndex = int(random.random() * len(A))  # RANDOM

    A[pivotIndex], A[0] = A[0], A[pivotIndex]

    L = 0
    R = len(A) - 1

    global num_comp
    num_comp += len(A) - 1

    # Partition A around a pivot
    P = A[L]
    i = L + 1
    for j in range(L+1, R+1):
        if A[j] < P:
            A[i], A[j] = A[j], A[i]
            i += 1
        else:
            pass

    A[L], A[i-1] = A[i-1], A[L]

    leftHalf = A[:i-1]
    rightHalf = A[i:R+1]
    A = quickSort(leftHalf, MODE) + [P] + quickSort(rightHalf, MODE)

    # num_comp += len(leftHalf) + len(rightHalf) - 2

    return A


def quickSort1(A):
    global num_comp
    # num_comp += len(A) - 1
    return quickSort(A, "FIRST")

def quickSort2(A):
    global num_comp
    # num_comp += len(A) - 1
    return quickSort(A, "LAST")

def quickSort3(A):
    global num_comp
    # num_comp += len(A) - 1
    return quickSort(A, "MEDIAN")



SIZE = 10000
test_input = []
for _ in range(SIZE):
    test_input.append(int(input()))

num_comp = 0
test_output1 = quickSort1(test_input[:])
print(num_comp)

num_comp = 0
test_output2 = quickSort2(test_input[:])
print(num_comp)

num_comp = 0
test_output3 = quickSort3(test_input[:])
print(num_comp)

assert(test_output1 == test_output2) and (test_output1 == test_output3)

"""
first n elements of 1.3.in: first last median

10: 25 31 21

100: 620 573 502

1000: 11175 10957 9735
"""
