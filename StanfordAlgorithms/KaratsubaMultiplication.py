from random import random
import math

def karatsubaMultiply(x, y):
    """
    Uses Karatsuba multiplication to multiply two large ints (recursively)
    """
    x, y = str(x), str(y)
    partition = max(len(x), len(y))//2

    # Base case
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)

    # (a*10^(partition) + b) * (c*10^(partition) + d)
    # = a*c*10^(partition + partition) + ((a+b)(c+d) - ac - bd)*10^(partition) + b*d

    a = int(x[:-partition]) if len(x) > partition else 0
    b = int(x[-partition:])
    c = int(y[:-partition]) if len(y) > partition else 0
    d = int(y[-partition:])

    ac = karatsubaMultiply(a, c)
    bd = karatsubaMultiply(b, d)
    abcd = karatsubaMultiply(a+b, c+d)
    part3 = (abcd - ac - bd) * 10**(partition)

    res = ac * 10**(2*partition) + part3 + bd

    print("ac:", ac, "bd:", bd, "abcd:", abcd, "part3", part3)
    print("{} * {} == {}".format(x, y, res))

    return res


for i in range(20):
    x = int(random() * 10**i)
    y = int(random() * 10**(i+1))
    res1 = x*y
    res2 = karatsubaMultiply(x, y)
    print("{}*{} ==> {} {}".format(x, y, res1, res2))
    print()

for _ in range(5):
    print()

x = 3141592653589793238462643383279502884197169399375105820974944592

y = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsubaMultiply(x,y))
print(x*y)