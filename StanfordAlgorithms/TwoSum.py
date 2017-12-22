
def TwoSum(nums, lowerBound, upperBound):
    """
    Returns num of nums in a RANGE from low to high which is the sum of two distinct nums

    Uses binary search since constant factor would be too high with regular Hash Table way

    Hash Table: O(TN), T = 2*10^4
    Binary Search: O(cNlogN), c the average length of SUBLIST of nums we will actually search

    With range of inputs R = 2*10^11, T = 2*10^4, N = 1*10^6

    c = N*(R/T) = 1

    and Binary Search method is 1000 times faster!

    Allowing for coefficients in Big-O, this is 2-3 orders of magnitude!
    ===> Consider the constants constraints when deciding the methods for implementation!

    """
    # Create hash set from nums
    nums = sorted(nums)
    results = set()

    # Uses binary search to find where in nums we should start searching
    # range is (n - upperBound, n - lowerBound)
    for i, n in enumerate(nums):

        start = lowerBound - n
        end = upperBound - n

        low = 0
        high = len(nums)

        while low < high:
            mid = low + (high - low)//2
            if nums[mid] < start:
                low = mid + 1
            elif nums[mid] >= start:
                high = mid - 1

        j = low
        while j < len(nums) and nums[j] <= end:
            sumij = nums[j] + n
            if i != j and sumij >= lowerBound and sumij not in results:
                results.add(sumij)
            j += 1

    return results


def TwoSumSingle(nums, target):
    """
    Returns whether a target number is the sum of any two distinct nums
    Uses hash table
    """
    for n in nums:
        if target - n != n and target - n in nums:
            return True
    return False


def alg(FNAME):
    with open(FNAME, "r") as f:
        lines = f.readlines()
        nums = [int(line.strip()) for line in lines]

    targetsFound = TwoSum(nums, -10000, 10000)
    res = len(targetsFound)

    return res


print(alg("2.4.in"))
