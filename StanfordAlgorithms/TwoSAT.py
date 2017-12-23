import random, math, copy

def TwoSAT(clauses):
    """
    Implements (naively) Papdimitriou's Algorithm

    Time: O(N^2 * log N)
    """

    random.seed()

    V = len(clauses)
    clauses = preprocess(clauses)
    N = len(clauses)

    if N <= 1:
        return 1

    # For log n iterations
    for _ in range(int(math.log(N, 2))):

        # Pick a random arrangement of variables
        variables = [bool(random.getrandbits(1)) for _ in range(V+1)]

        # For 2*n^2 iterations.
        for __ in range(2*N**2):
            # Check satisfiability
            if checkSatisfies(variables, clauses):
                return 1

    return 0

def checkSatisfies(variables, clauses):

    # print("Checking variables: {}".format(variables))

    # Checks all clauses for satisfaction
    for a, b in clauses:

        satisfyA = variables[a] if a > 0 else not variables[-a]
        satisfyB = variables[b] if b > 0 else not variables[-b]

        a, b = abs(a), abs(b)

        # print("Clause: {}, satisfyA: {}, satisfyB: {}, (vars): {}".format((a,b),satisfyA,satisfyB, (variables[a],variables[b])))

        # If clause not satisfied, Flips random variable (1 of the 2)
        if not satisfyA and not satisfyB:
            flipA = bool(random.getrandbits(1))
            if flipA:
                variables[a] = not variables[a]
            else:
                variables[b] = not variables[b]
            return False

    # print("Clauses: {}".format(clauses))
    # print("Variables: {}".format(variables))
    return True


def preprocess(clauses):
    """
    Find fixed values for variables with a single representation

    Remove clauses which are trivially satisfied

    A further optimization would be to fix those variables with True/False,
    and not randomize those variables in TwoSAT function
    """

    V = len(clauses)    # num variables
    found = True

    while found:
        found = False

        new_clauses = []

        varTrue = [False for i in range(V+1)]
        varFalse = [False for i in range(V+1)]

        # Determine variable representations
        for a, b in clauses:
            if a > 0:
                varTrue[a] = True
            else:
                varFalse[-a] = True

            if b > 0:
                varTrue[b] = True
            else:
                varFalse[-b] = True

        # Remove trivially satisfied clauses
        for a, b in clauses:
            if (varTrue[abs(a)] and varFalse[abs(a)]) and (varTrue[abs(b)] and varFalse[abs(b)]):
                new_clauses.append((a, b))
            else:
                found = True

        clauses = new_clauses

        # print("varTrue: {}, varFalse: {}".format(varTrue, varFalse))
        # print("Clauses: {}".format(clauses))

    print("Clauses reduced to length: {}".format(len(clauses)))

    return clauses



def alg(FNAME):

    with open(FNAME, "r") as fin:

        lines = fin.readlines()
        # input constructed s.t. # variables = # clauses
        V = int(lines[0].strip())
        clauses = [[int(x) for x in line.split()] for line in lines[1:]]

    res = TwoSAT(clauses)

    return res


# for i in ['a','b','c','d','e','f']:
#     print(alg("4.4"+i+".txt"))
