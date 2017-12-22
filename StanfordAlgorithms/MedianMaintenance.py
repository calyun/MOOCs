
from heapq import *
# Actually, PriorityQueue is a thread-safe, queue-based wrapper of heapq

def medianMaintenance(nums):
    """
    Note: For Python heapq, a minheap is used, so to make a maxheap, you must invert the values
    """
    lowHeap = []
    highHeap = []
    medians = []
    highSize = 0
    lowSize = 0

    for n in nums:
        highMin = highHeap[0] if highSize >= 1 else 999999

        # add to low heap
        if n <= highMin:
            heappush(lowHeap, -n)
            lowSize += 1

            if lowSize >= highSize + 2:
                heappush(highHeap, -heappop(lowHeap))
                lowSize -= 1
                highSize += 1

        else:
            heappush(highHeap, n)
            highSize += 1

            if highSize > lowSize:
                heappush(lowHeap, -heappop(highHeap))
                lowSize += 1
                highSize -= 1

        median = -lowHeap[0]
        medians.append(median)

    return medians


def alg(FNAME):
    with open(FNAME, "r") as f:
        lines = f.readlines()
        nums = [int(line.strip()) for line in lines]

    medians = medianMaintenance(nums)
    res = sum(medians) % 10000

    return res

print(alg("2.3.in"))
